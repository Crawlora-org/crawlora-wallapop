# Crawlora Wallapop API client for Ruby (`crawlora-wallapop`)

This Ruby gem calls Crawlora's hosted Wallapop API at `https://api.crawlora.net/api/v1`. It exposes 5 endpoints covering public listing search, categories, filters, and item details; it does not call or scrape Wallapop directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-wallapop"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/wallapop"

client = Crawlora::Wallapop::Client.new
result = client.request("wallapop-search", JSON.parse("{\"q\": \"sample\", \"latitude\": 1.0, \"longitude\": 1.0}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 5 API operations.

```ruby
client = Crawlora::Wallapop::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Wallapop API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-wallapop/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/wallapop/categories` | `wallapop-categories` | Discover Wallapop search categories |
| `GET` | `/wallapop/filter-options` | `wallapop-filter-options` | Discover Wallapop remote filter values |
| `GET` | `/wallapop/filters` | `wallapop-filters` | Discover Wallapop search filters |
| `GET` | `/wallapop/item` | `wallapop-item-detail` | Fetch a public Wallapop listing detail page |
| `GET` | `/wallapop/search` | `wallapop-search` | Search Wallapop public listings |

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-wallapop) for account setup, the API operation reference, and release history.
