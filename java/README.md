# Crawlora Wallapop API client for Java

The official Java client for Crawlora's hosted Wallapop API. It exposes 5 endpoints covering public listing search, categories, filters, and item details. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-wallapop</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-java-console) to get an API key.

```java
import net.crawlora.wallapop.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.categories(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Wallapop API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-wallapop/blob/main/docs/usage.md) also lists parameters and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/wallapop/categories` | `wallapop-categories` | Discover Wallapop search categories |
| `GET` | `/wallapop/filter-options` | `wallapop-filter-options` | Discover Wallapop remote filter values |
| `GET` | `/wallapop/filters` | `wallapop-filters` | Discover Wallapop search filters |
| `GET` | `/wallapop/item` | `wallapop-item-detail` | Fetch a public Wallapop listing detail page |
| `GET` | `/wallapop/search` | `wallapop-search` | Search Wallapop public listings |

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-wallapop)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-java-api-docs)
