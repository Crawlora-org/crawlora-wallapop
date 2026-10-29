# Crawlora Wallapop JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `5`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| wallapop | `wallapop.categories` | `wallapop-categories` | `GET /wallapop/categories` | none | `ApiKeyAuth` | `WallapopCategoriesResponse` |  |
| wallapop | `wallapop.filterOptions` | `wallapop-filter-options` | `GET /wallapop/filter-options` | `filter_id` (query string required)<br>`category_id` (query number required)<br>`brand` (query string)<br>`q` (query string)<br>`sort` (query "closest" \| "most_relevance" \| "newest" \| "price_low_to_high" \| "price_high_to_low")<br>`options_query` (query string)<br>`cursor` (query string) | `ApiKeyAuth` | `WallapopFilterOptionsResponse` |  |
| wallapop | `wallapop.filters` | `wallapop-filters` | `GET /wallapop/filters` | `q` (query string)<br>`category_id` (query number) | `ApiKeyAuth` | `WallapopFiltersResponse` |  |
| wallapop | `wallapop.itemDetail` | `wallapop-item-detail` | `GET /wallapop/item` | `url` (query string required) | `ApiKeyAuth` | `WallapopItemDetailResponse` |  |
| wallapop | `wallapop.search` | `wallapop-search` | `GET /wallapop/search` | `q` (query string required)<br>`latitude` (query number required)<br>`longitude` (query number required)<br>`category_id` (query number)<br>`sort` (query "closest" \| "most_relevance" \| "newest" \| "price_low_to_high" \| "price_high_to_low")<br>`min_price` (query number)<br>`max_price` (query number)<br>`condition` (query string)<br>`is_shippable` (query "true")<br>`time_filter` (query "today" \| "lastWeek" \| "lastMonth")<br>`distance_in_km` (query number)<br>`filter` (query Array<string>)<br>`cursor` (query string) | `ApiKeyAuth` | `WallapopSearchResponse` |  |
