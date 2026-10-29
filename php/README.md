# Crawlora Wallapop API client for PHP (`crawlora/wallapop`)

This PHP package calls Crawlora's hosted Wallapop API at `https://api.crawlora.net/api/v1`. It exposes 5 endpoints covering public listing search, categories, filters, and item details. It does not call or scrape Wallapop directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/wallapop
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Wallapop\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("wallapop-search", ['q' => 'sample', 'latitude' => 1.0, 'longitude' => 1.0]);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 5 API operations.

## Supported Wallapop API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-wallapop/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/wallapop/categories` | `wallapop-categories` | Discover Wallapop search categories |
| `GET` | `/wallapop/filter-options` | `wallapop-filter-options` | Discover Wallapop remote filter values |
| `GET` | `/wallapop/filters` | `wallapop-filters` | Discover Wallapop search filters |
| `GET` | `/wallapop/item` | `wallapop-item-detail` | Fetch a public Wallapop listing detail page |
| `GET` | `/wallapop/search` | `wallapop-search` | Search Wallapop public listings |

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-wallapop). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-wallapop/blob/main/docs/usage.md).
