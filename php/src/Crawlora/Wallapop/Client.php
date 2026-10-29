<?php

declare(strict_types=1);

namespace Crawlora\Wallapop;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'wallapop';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 5;
    public const OPERATION_IDS = ["wallapop-categories", "wallapop-filter-options", "wallapop-filters", "wallapop-item-detail", "wallapop-search"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"wallapop-categories": {"bodyParam": null, "bodyRequired": false, "id": "wallapop-categories", "method": "GET", "params": [], "path": "/wallapop/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "wallapop-filter-options": {"bodyParam": null, "bodyRequired": false, "id": "wallapop-filter-options", "method": "GET", "params": [{"description": "Remote filter ID advertised by /wallapop/filters for this category", "in": "query", "name": "filter_id", "required": true, "type": "string", "x-example": "item_language"}, {"description": "Live category ID from /wallapop/categories. Use a root for brand/model or the selected category for category-specific remote options.", "in": "query", "name": "category_id", "required": true, "type": "integer", "x-example": 24100}, {"description": "Required with filter_id=model; a brand option ID", "in": "query", "name": "brand", "type": "string", "x-example": "BMW"}, {"description": "Optional listing search context", "in": "query", "name": "q", "type": "string", "x-example": "iphone"}, {"description": "Optional listing sort context", "enum": ["closest", "most_relevance", "newest", "price_low_to_high", "price_high_to_low"], "in": "query", "name": "sort", "type": "string", "x-example": "most_relevance"}, {"description": "Optional text search inside the dynamic option list", "in": "query", "name": "options_query", "type": "string", "x-example": "BMW"}, {"description": "Opaque next_cursor returned by this endpoint", "in": "query", "name": "cursor", "type": "string"}], "path": "/wallapop/filter-options", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "filter_id", "required": true, "type": "string"}, {"in": "query", "name": "category_id", "required": true, "type": "integer"}, {"in": "query", "name": "brand", "type": "string"}, {"in": "query", "name": "q", "type": "string"}, {"enum": ["closest", "most_relevance", "newest", "price_low_to_high", "price_high_to_low"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "options_query", "type": "string"}, {"in": "query", "name": "cursor", "type": "string"}], "security": ["ApiKeyAuth"]}, "wallapop-filters": {"bodyParam": null, "bodyRequired": false, "id": "wallapop-filters", "method": "GET", "params": [{"description": "Optional search phrase used to select relevant filters", "in": "query", "name": "q", "type": "string", "x-example": "iphone"}, {"description": "Any live search taxonomy ID from /wallapop/categories", "in": "query", "name": "category_id", "type": "integer", "x-example": 100}], "path": "/wallapop/filters", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "type": "string"}, {"in": "query", "name": "category_id", "type": "integer"}], "security": ["ApiKeyAuth"]}, "wallapop-item-detail": {"bodyParam": null, "bodyRequired": false, "id": "wallapop-item-detail", "method": "GET", "params": [{"description": "Clean https public item URL from /wallapop/search on es.wallapop.com, it.wallapop.com, or pt.wallapop.com", "in": "query", "name": "url", "required": true, "type": "string", "x-example": "https%3A%2F%2Fes.wallapop.com%2Fitem%2Fchaqueta-1183989904"}], "path": "/wallapop/item", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "wallapop-search": {"bodyParam": null, "bodyRequired": false, "id": "wallapop-search", "method": "GET", "params": [{"description": "Free-text listing search, 2 to 200 characters", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "iphone"}, {"description": "Caller-provided search latitude, -90 through 90", "in": "query", "name": "latitude", "required": true, "type": "number", "x-example": 40.4168}, {"description": "Caller-provided search longitude, -180 through 180", "in": "query", "name": "longitude", "required": true, "type": "number", "x-example": -3.7038}, {"description": "Any live search taxonomy ID from /wallapop/categories", "in": "query", "name": "category_id", "type": "integer", "x-example": 24200}, {"description": "Wallapop sort order", "enum": ["closest", "most_relevance", "newest", "price_low_to_high", "price_high_to_low"], "in": "query", "name": "sort", "type": "string", "x-example": "most_relevance"}, {"description": "Minimum sale price", "in": "query", "name": "min_price", "type": "number", "x-example": 10}, {"description": "Maximum sale price", "in": "query", "name": "max_price", "type": "number", "x-example": 500}, {"description": "Repeatable or comma-separated condition values. With category_id, use the current values from /wallapop/filters; without category_id, base values are new, as_good_as_new, good, fair, and has_given_it_all.", "in": "query", "name": "condition", "type": "string", "x-example": "new,good"}, {"description": "Pass true to limit to shipping-capable listings; omit to include all. false is rejected because Wallapop ignores it.", "enum": ["true"], "in": "query", "name": "is_shippable", "type": "string", "x-example": "true"}, {"description": "Listing date window", "enum": ["today", "lastWeek", "lastMonth"], "in": "query", "name": "time_filter", "type": "string", "x-example": "lastWeek"}, {"description": "Maximum distance from the supplied coordinates, 0 through 1000 km", "in": "query", "name": "distance_in_km", "type": "integer", "x-example": 25}, {"collectionFormat": "csv", "description": "Repeatable category-specific key:value pair discovered from /wallapop/filters, e.g. brand:BMW, color:Black, has_warranty:true, storage_capacity:128gb, item_language:english, or fashion_size:3,4. For remote values use IDs returned by /wallapop/filter-options.", "in": "query", "items": {"type": "string"}, "name": "filter", "type": "array", "x-example": "storage_capacity:128gb"}, {"description": "Opaque next_cursor returned by a previous response. Use it alone, without initial search parameters.", "in": "query", "name": "cursor", "type": "string", "x-example": "eyJ2IjoxLCJuZXh0X3BhZ2UiOiJ..."}], "path": "/wallapop/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "latitude", "required": true, "type": "number"}, {"in": "query", "name": "longitude", "required": true, "type": "number"}, {"in": "query", "name": "category_id", "type": "integer"}, {"enum": ["closest", "most_relevance", "newest", "price_low_to_high", "price_high_to_low"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "min_price", "type": "number"}, {"in": "query", "name": "max_price", "type": "number"}, {"in": "query", "name": "condition", "type": "string"}, {"enum": ["true"], "in": "query", "name": "is_shippable", "type": "string"}, {"enum": ["today", "lastWeek", "lastMonth"], "in": "query", "name": "time_filter", "type": "string"}, {"in": "query", "name": "distance_in_km", "type": "integer"}, {"collectionFormat": "csv", "in": "query", "name": "filter", "type": "array"}, {"in": "query", "name": "cursor", "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-wallapop-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wallapop-categories", $params, $responseType);
    }
    public function filter_options(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wallapop-filter-options", $params, $responseType);
    }
    public function filters(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wallapop-filters", $params, $responseType);
    }
    public function item_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wallapop-item-detail", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wallapop-search", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
