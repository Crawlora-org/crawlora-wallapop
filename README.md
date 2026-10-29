# Wallapop clients for Crawlora

Official Crawlora client packages for the hosted Wallapop API. Access 5 API endpoints covering public listing search, categories, filters, and item details from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape Wallapop locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Wallapop or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/wallapop`](javascript/README.md)
- Python: [`crawlora-wallapop`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-wallapop`](go.mod)
- Ruby: [`crawlora-wallapop`](ruby/README.md)
- Java: [`net.crawlora:crawlora-wallapop:0.1.0`](java/README.md)
- PHP: [`crawlora/wallapop`](php/README.md)
- Rust: [`crawlora-wallapop`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 5 selected public Wallapop API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/wallapop/categories` | `wallapop-categories` | Discover Wallapop search categories |
| `GET` | `/wallapop/filter-options` | `wallapop-filter-options` | Discover Wallapop remote filter values |
| `GET` | `/wallapop/filters` | `wallapop-filters` | Discover Wallapop search filters |
| `GET` | `/wallapop/item` | `wallapop-item-detail` | Fetch a public Wallapop listing detail page |
| `GET` | `/wallapop/search` | `wallapop-search` | Search Wallapop public listings |

## License

MIT. See [LICENSE](LICENSE).
