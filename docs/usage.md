# Wallapop API endpoint reference and client usage

This reference lists all 5 public Wallapop API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/wallapop`, `crawlora-wallapop`, and `crawlora-wallapop` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Wallapop locally; Crawlora is independent from and not endorsed by Wallapop or its owners.

The package tracks the public API contract revision `sha256:b02fd52a304c711998d8723a17adfd9b3eb7815d77f444a3f276679cf8ff4019` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `wallapop`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `categories` | `categories` | `wallapop.categories` | `GET /wallapop/categories` | — | Discover Wallapop search categories |
| `filterOptions` | `filter_options` | `wallapop.filter_options` | `GET /wallapop/filter-options` | `filter_id` (query, required), `category_id` (query, required), `brand` (query, optional), `q` (query, optional), `sort` (query, optional; values: `closest`, `most_relevance`, `newest`, `price_low_to_high`, `price_high_to_low`), `options_query` (query, optional), `cursor` (query, optional) | Discover Wallapop remote filter values |
| `filters` | `filters` | `wallapop.filters` | `GET /wallapop/filters` | `q` (query, optional), `category_id` (query, optional) | Discover Wallapop search filters |
| `itemDetail` | `item_detail` | `wallapop.item_detail` | `GET /wallapop/item` | `url` (query, required) | Fetch a public Wallapop listing detail page |
| `search` | `search` | `wallapop.search` | `GET /wallapop/search` | `q` (query, required), `latitude` (query, required), `longitude` (query, required), `category_id` (query, optional), `sort` (query, optional; values: `closest`, `most_relevance`, `newest`, `price_low_to_high`, `price_high_to_low`), `min_price` (query, optional), `max_price` (query, optional), `condition` (query, optional), `is_shippable` (query, optional; values: `true`), `time_filter` (query, optional; values: `today`, `lastWeek`, `lastMonth`), `distance_in_km` (query, optional), `filter` (query, optional), `cursor` (query, optional) | Search Wallapop public listings |

## Client forms

- JavaScript: import `WallapopClient` (also exported as `Client`) from `@crawlora-org/wallapop`; use `new WallapopClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `WallapopClient` (also exported as `Client`) from `crawlora_wallapop`; use `with WallapopClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncWallapopClient`, used with `async with` and `await`.
- Rust: add `crawlora-wallapop` with Cargo; import `Client` and the generated operation parameter struct, then call `client.wallapop.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-wallapop/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
