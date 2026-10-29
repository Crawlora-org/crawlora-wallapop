# Crawlora Wallapop Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `5`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| wallapop | `wallapop.categories` | `wallapop-categories` | `GET /wallapop/categories` | none | `ApiKeyAuth` | `WallapopCategoriesResponse` |  |
| wallapop | `wallapop.filter_options` | `wallapop-filter-options` | `GET /wallapop/filter-options` | `filter_id` (query String required)<br>`category_id` (query i64 required)<br>`brand` (query String)<br>`q` (query String)<br>`sort` (query String enum{closest, most_relevance, newest, price_low_to_high, price_high_to_low})<br>`options_query` (query String)<br>`cursor` (query String) | `ApiKeyAuth` | `WallapopFilterOptionsResponse` |  |
| wallapop | `wallapop.filters` | `wallapop-filters` | `GET /wallapop/filters` | `q` (query String)<br>`category_id` (query i64) | `ApiKeyAuth` | `WallapopFiltersResponse` |  |
| wallapop | `wallapop.item_detail` | `wallapop-item-detail` | `GET /wallapop/item` | `url` (query String required) | `ApiKeyAuth` | `WallapopItemDetailResponse` |  |
| wallapop | `wallapop.search` | `wallapop-search` | `GET /wallapop/search` | `q` (query String required)<br>`latitude` (query f64 required)<br>`longitude` (query f64 required)<br>`category_id` (query i64)<br>`sort` (query String enum{closest, most_relevance, newest, price_low_to_high, price_high_to_low})<br>`min_price` (query f64)<br>`max_price` (query f64)<br>`condition` (query String)<br>`is_shippable` (query String enum{true})<br>`time_filter` (query String enum{today, lastWeek, lastMonth})<br>`distance_in_km` (query i64)<br>`filter` (query Vec<String>)<br>`cursor` (query String) | `ApiKeyAuth` | `WallapopSearchResponse` |  |
