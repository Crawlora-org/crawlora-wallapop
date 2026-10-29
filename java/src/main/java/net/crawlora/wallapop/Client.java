package net.crawlora.wallapop;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the Wallapop endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 5;
    public static final List<String> OPERATION_IDS = List.of(
            "wallapop-categories",
            "wallapop-filter-options",
            "wallapop-filters",
            "wallapop-item-detail",
            "wallapop-search"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("wallapop-categories", new Operation("wallapop-categories", "GET", "/wallapop/categories", Map.of(), List.of("application/json")));
        operations.put("wallapop-filter-options", new Operation("wallapop-filter-options", "GET", "/wallapop/filter-options", Map.ofEntries(Map.entry("filter_id", new Param("filter_id", "query", true, "string", List.of(), "csv")), Map.entry("category_id", new Param("category_id", "query", true, "integer", List.of(), "csv")), Map.entry("brand", new Param("brand", "query", false, "string", List.of(), "csv")), Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("closest", "most_relevance", "newest", "price_low_to_high", "price_high_to_low"), "csv")), Map.entry("options_query", new Param("options_query", "query", false, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("wallapop-filters", new Operation("wallapop-filters", "GET", "/wallapop/filters", Map.ofEntries(Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv")), Map.entry("category_id", new Param("category_id", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("wallapop-item-detail", new Operation("wallapop-item-detail", "GET", "/wallapop/item", Map.ofEntries(Map.entry("url", new Param("url", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("wallapop-search", new Operation("wallapop-search", "GET", "/wallapop/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("latitude", new Param("latitude", "query", true, "number", List.of(), "csv")), Map.entry("longitude", new Param("longitude", "query", true, "number", List.of(), "csv")), Map.entry("category_id", new Param("category_id", "query", false, "integer", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("closest", "most_relevance", "newest", "price_low_to_high", "price_high_to_low"), "csv")), Map.entry("min_price", new Param("min_price", "query", false, "number", List.of(), "csv")), Map.entry("max_price", new Param("max_price", "query", false, "number", List.of(), "csv")), Map.entry("condition", new Param("condition", "query", false, "string", List.of(), "csv")), Map.entry("is_shippable", new Param("is_shippable", "query", false, "string", List.of("true"), "csv")), Map.entry("time_filter", new Param("time_filter", "query", false, "string", List.of("today", "lastWeek", "lastMonth"), "csv")), Map.entry("distance_in_km", new Param("distance_in_km", "query", false, "integer", List.of(), "csv")), Map.entry("filter", new Param("filter", "query", false, "array", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown Wallapop operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object categories(Map<String, ?> params) { return request("wallapop-categories", params); }
    public Object filterOptions(Map<String, ?> params) { return request("wallapop-filter-options", params); }
    public Object filters(Map<String, ?> params) { return request("wallapop-filters", params); }
    public Object itemDetail(Map<String, ?> params) { return request("wallapop-item-detail", params); }
    public Object search(Map<String, ?> params) { return request("wallapop-search", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
