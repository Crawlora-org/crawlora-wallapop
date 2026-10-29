from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelWallapopSearchResponseDoc = TypedDict('ModelWallapopSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWallapopSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWallapopSearchResponse = TypedDict('ModelWallapopSearchResponse', {
    'category_id': NotRequired[int],
    'count': NotRequired[int],
    'country_code': NotRequired[str],
    'fetched_at': NotRequired[str],
    'items': NotRequired[list[ModelWallapopListingCard]],
    'next_cursor': NotRequired[str],
    'query': NotRequired[str],
    'sort': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelWallapopListingCard = TypedDict('ModelWallapopListingCard', {
    'category_id': NotRequired[int],
    'currency': NotRequired[str],
    'id': NotRequired[str],
    'images': NotRequired[list[str]],
    'location': NotRequired[ModelWallapopListingLocation],
    'price': NotRequired[float],
    'shipping': NotRequired[ModelWallapopListingShipping],
    'slug': NotRequired[str],
    'taxonomy': NotRequired[list[ModelWallapopListingTaxonomy]],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelWallapopListingTaxonomy = TypedDict('ModelWallapopListingTaxonomy', {
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelWallapopListingShipping = TypedDict('ModelWallapopListingShipping', {
    'item_is_shippable': NotRequired[bool],
    'user_allows_shipping': NotRequired[bool],
}, total=False)

ModelWallapopListingLocation = TypedDict('ModelWallapopListingLocation', {
    'city': NotRequired[str],
    'country_code': NotRequired[str],
    'region': NotRequired[str],
    'region2': NotRequired[str],
}, total=False)

ModelWallapopItemDetailResponseDoc = TypedDict('ModelWallapopItemDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWallapopItemDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWallapopItemDetailResponse = TypedDict('ModelWallapopItemDetailResponse', {
    'attributes': NotRequired[list[ModelWallapopItemDetailAttribute]],
    'category_id': NotRequired[int],
    'characteristics': NotRequired[list[ModelWallapopItemDetailCharacteristic]],
    'condition': NotRequired[ModelWallapopItemDetailCondition],
    'currency': NotRequired[str],
    'description': NotRequired[str],
    'fetched_at': NotRequired[str],
    'hashtags': NotRequired[list[str]],
    'id': NotRequired[str],
    'images': NotRequired[list[str]],
    'location': NotRequired[ModelWallapopListingLocation],
    'price': NotRequired[float],
    'related_searches': NotRequired[list[ModelWallapopItemDetailRelatedSearch]],
    'shipping': NotRequired[ModelWallapopListingShipping],
    'slug': NotRequired[str],
    'taxonomy': NotRequired[list[ModelWallapopListingTaxonomy]],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelWallapopItemDetailRelatedSearch = TypedDict('ModelWallapopItemDetailRelatedSearch', {
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelWallapopItemDetailCondition = TypedDict('ModelWallapopItemDetailCondition', {
    'text': NotRequired[str],
    'title': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelWallapopItemDetailCharacteristic = TypedDict('ModelWallapopItemDetailCharacteristic', {
    'attribute': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelWallapopItemDetailAttribute = TypedDict('ModelWallapopItemDetailAttribute', {
    'key': NotRequired[str],
    'text': NotRequired[str],
    'title': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelWallapopFiltersResponseDoc = TypedDict('ModelWallapopFiltersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWallapopFiltersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWallapopFiltersResponse = TypedDict('ModelWallapopFiltersResponse', {
    'category_id': NotRequired[int],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'filters': NotRequired[list[ModelWallapopFilterDefinition]],
    'query': NotRequired[str],
    'root_category_id': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelWallapopFilterDefinition = TypedDict('ModelWallapopFilterDefinition', {
    'format': NotRequired[str],
    'id': NotRequired[str],
    'is_search_enabled': NotRequired[bool],
    'label': NotRequired[str],
    'options': NotRequired[list[ModelWallapopFilterOption]],
    'options_endpoint': NotRequired[str],
    'reload_when_changed': NotRequired[bool],
    'search_params': NotRequired[dict[str, ModelWallapopFilterParamBinding]],
    'selection': NotRequired[str],
    'source': NotRequired[str],
    'steps': NotRequired[list[ModelWallapopFilterRangeStep]],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'unit': NotRequired[str],
}, total=False)

ModelWallapopFilterRangeStep = TypedDict('ModelWallapopFilterRangeStep', {
    'end': NotRequired[float],
    'increment': NotRequired[float],
    'start': NotRequired[float],
}, total=False)

ModelWallapopFilterParamBinding = TypedDict('ModelWallapopFilterParamBinding', {
    'param_key': NotRequired[str],
    'param_value': NotRequired[str],
}, total=False)

ModelWallapopFilterOption = TypedDict('ModelWallapopFilterOption', {
    'id': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelWallapopFilterOptionsResponseDoc = TypedDict('ModelWallapopFilterOptionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWallapopFilterOptionsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWallapopFilterOptionsResponse = TypedDict('ModelWallapopFilterOptionsResponse', {
    'brand': NotRequired[str],
    'category_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'filter_id': NotRequired[str],
    'next_cursor': NotRequired[str],
    'options': NotRequired[list[ModelWallapopFilterOption]],
    'options_query': NotRequired[str],
    'page_size': NotRequired[int],
    'q': NotRequired[str],
    'sort': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelWallapopCategoriesResponseDoc = TypedDict('ModelWallapopCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWallapopCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWallapopCategoriesResponse = TypedDict('ModelWallapopCategoriesResponse', {
    'categories': NotRequired[list[ModelWallapopCategory]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'max_depth': NotRequired[int],
    'root_count': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelWallapopCategory = TypedDict('ModelWallapopCategory', {
    'depth': NotRequired[int],
    'id': NotRequired[int],
    'is_leaf': NotRequired[bool],
    'name': NotRequired[str],
    'parent_id': NotRequired[int],
    'path': NotRequired[str],
    'root_id': NotRequired[int],
    'vertical_id': NotRequired[str],
}, total=False)

WallapopCategoriesResponse = ModelWallapopCategoriesResponseDoc
WallapopCategoriesParams = TypedDict('WallapopCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

WallapopFilterOptionsResponse = ModelWallapopFilterOptionsResponseDoc
WallapopFilterOptionsParams = TypedDict('WallapopFilterOptionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'filter_id': Required[str],
    'category_id': Required[int],
    'brand': NotRequired[str],
    'q': NotRequired[str],
    'sort': NotRequired[Literal['closest', 'most_relevance', 'newest', 'price_low_to_high', 'price_high_to_low']],
    'options_query': NotRequired[str],
    'cursor': NotRequired[str],
}, total=False)

WallapopFiltersResponse = ModelWallapopFiltersResponseDoc
WallapopFiltersParams = TypedDict('WallapopFiltersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': NotRequired[str],
    'category_id': NotRequired[int],
}, total=False)

WallapopItemDetailResponse = ModelWallapopItemDetailResponseDoc
WallapopItemDetailParams = TypedDict('WallapopItemDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
}, total=False)

WallapopSearchResponse = ModelWallapopSearchResponseDoc
WallapopSearchParams = TypedDict('WallapopSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'latitude': Required[float],
    'longitude': Required[float],
    'category_id': NotRequired[int],
    'sort': NotRequired[Literal['closest', 'most_relevance', 'newest', 'price_low_to_high', 'price_high_to_low']],
    'min_price': NotRequired[float],
    'max_price': NotRequired[float],
    'condition': NotRequired[str],
    'is_shippable': NotRequired[Literal['true']],
    'time_filter': NotRequired[Literal['today', 'lastWeek', 'lastMonth']],
    'distance_in_km': NotRequired[int],
    'filter': NotRequired[list[str]],
    'cursor': NotRequired[str],
}, total=False)

class WallapopGroup:
    @overload
    def categories(self, **params: Unpack[WallapopCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[WallapopCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[WallapopCategoriesDefaultParams]) -> WallapopCategoriesResponse: ...
    @overload
    def filter_options(self, **params: Unpack[WallapopFilterOptionsStreamParams]) -> BinaryIO: ...
    @overload
    def filter_options(self, **params: Unpack[WallapopFilterOptionsTextResponseParams]) -> str: ...
    @overload
    def filter_options(self, **params: Unpack[WallapopFilterOptionsDefaultParams]) -> WallapopFilterOptionsResponse: ...
    @overload
    def filters(self, **params: Unpack[WallapopFiltersStreamParams]) -> BinaryIO: ...
    @overload
    def filters(self, **params: Unpack[WallapopFiltersTextResponseParams]) -> str: ...
    @overload
    def filters(self, **params: Unpack[WallapopFiltersDefaultParams]) -> WallapopFiltersResponse: ...
    @overload
    def item_detail(self, **params: Unpack[WallapopItemDetailStreamParams]) -> BinaryIO: ...
    @overload
    def item_detail(self, **params: Unpack[WallapopItemDetailTextResponseParams]) -> str: ...
    @overload
    def item_detail(self, **params: Unpack[WallapopItemDetailDefaultParams]) -> WallapopItemDetailResponse: ...
    @overload
    def search(self, **params: Unpack[WallapopSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[WallapopSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[WallapopSearchDefaultParams]) -> WallapopSearchResponse: ...

OperationId = Literal[
    'wallapop-categories',
    'wallapop-filter-options',
    'wallapop-filters',
    'wallapop-item-detail',
    'wallapop-search',
]

class CrawloraClient:
    wallapop: WallapopGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wallapop-categories'],
        params: WallapopCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WallapopCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wallapop-filter-options'],
        params: WallapopFilterOptionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WallapopFilterOptionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wallapop-filters'],
        params: WallapopFiltersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WallapopFiltersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wallapop-item-detail'],
        params: WallapopItemDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WallapopItemDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wallapop-search'],
        params: WallapopSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WallapopSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['wallapop-categories'],
        params: WallapopCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WallapopCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['wallapop-filter-options'],
        params: WallapopFilterOptionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WallapopFilterOptionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['wallapop-filters'],
        params: WallapopFiltersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WallapopFiltersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['wallapop-item-detail'],
        params: WallapopItemDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WallapopItemDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['wallapop-search'],
        params: WallapopSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WallapopSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class WallapopClient(CrawloraClient):
    def __enter__(self) -> WallapopClient: ...
    @overload
    def categories(self, **params: Unpack[WallapopCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[WallapopCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[WallapopCategoriesDefaultParams]) -> WallapopCategoriesResponse: ...
    @overload
    def filter_options(self, **params: Unpack[WallapopFilterOptionsStreamParams]) -> BinaryIO: ...
    @overload
    def filter_options(self, **params: Unpack[WallapopFilterOptionsTextResponseParams]) -> str: ...
    @overload
    def filter_options(self, **params: Unpack[WallapopFilterOptionsDefaultParams]) -> WallapopFilterOptionsResponse: ...
    @overload
    def filters(self, **params: Unpack[WallapopFiltersStreamParams]) -> BinaryIO: ...
    @overload
    def filters(self, **params: Unpack[WallapopFiltersTextResponseParams]) -> str: ...
    @overload
    def filters(self, **params: Unpack[WallapopFiltersDefaultParams]) -> WallapopFiltersResponse: ...
    @overload
    def item_detail(self, **params: Unpack[WallapopItemDetailStreamParams]) -> BinaryIO: ...
    @overload
    def item_detail(self, **params: Unpack[WallapopItemDetailTextResponseParams]) -> str: ...
    @overload
    def item_detail(self, **params: Unpack[WallapopItemDetailDefaultParams]) -> WallapopItemDetailResponse: ...
    @overload
    def search(self, **params: Unpack[WallapopSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[WallapopSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[WallapopSearchDefaultParams]) -> WallapopSearchResponse: ...

class AsyncWallapopClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncWallapopClient: ...
    wallapop: _AsyncWallapopGroup
    @overload
    async def categories(self, **params: Unpack[WallapopCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[WallapopCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[WallapopCategoriesDefaultParams]) -> WallapopCategoriesResponse: ...
    @overload
    async def filter_options(self, **params: Unpack[WallapopFilterOptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def filter_options(self, **params: Unpack[WallapopFilterOptionsTextResponseParams]) -> str: ...
    @overload
    async def filter_options(self, **params: Unpack[WallapopFilterOptionsDefaultParams]) -> WallapopFilterOptionsResponse: ...
    @overload
    async def filters(self, **params: Unpack[WallapopFiltersStreamParams]) -> BinaryIO: ...
    @overload
    async def filters(self, **params: Unpack[WallapopFiltersTextResponseParams]) -> str: ...
    @overload
    async def filters(self, **params: Unpack[WallapopFiltersDefaultParams]) -> WallapopFiltersResponse: ...
    @overload
    async def item_detail(self, **params: Unpack[WallapopItemDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def item_detail(self, **params: Unpack[WallapopItemDetailTextResponseParams]) -> str: ...
    @overload
    async def item_detail(self, **params: Unpack[WallapopItemDetailDefaultParams]) -> WallapopItemDetailResponse: ...
    @overload
    async def search(self, **params: Unpack[WallapopSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[WallapopSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[WallapopSearchDefaultParams]) -> WallapopSearchResponse: ...

class _AsyncWallapopGroup:
    @overload
    async def categories(self, **params: Unpack[WallapopCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[WallapopCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[WallapopCategoriesDefaultParams]) -> WallapopCategoriesResponse: ...
    @overload
    async def filter_options(self, **params: Unpack[WallapopFilterOptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def filter_options(self, **params: Unpack[WallapopFilterOptionsTextResponseParams]) -> str: ...
    @overload
    async def filter_options(self, **params: Unpack[WallapopFilterOptionsDefaultParams]) -> WallapopFilterOptionsResponse: ...
    @overload
    async def filters(self, **params: Unpack[WallapopFiltersStreamParams]) -> BinaryIO: ...
    @overload
    async def filters(self, **params: Unpack[WallapopFiltersTextResponseParams]) -> str: ...
    @overload
    async def filters(self, **params: Unpack[WallapopFiltersDefaultParams]) -> WallapopFiltersResponse: ...
    @overload
    async def item_detail(self, **params: Unpack[WallapopItemDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def item_detail(self, **params: Unpack[WallapopItemDetailTextResponseParams]) -> str: ...
    @overload
    async def item_detail(self, **params: Unpack[WallapopItemDetailDefaultParams]) -> WallapopItemDetailResponse: ...
    @overload
    async def search(self, **params: Unpack[WallapopSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[WallapopSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[WallapopSearchDefaultParams]) -> WallapopSearchResponse: ...

WallapopCategoriesDefaultParams = TypedDict('WallapopCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

WallapopCategoriesTextResponseParams = TypedDict('WallapopCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

WallapopCategoriesStreamParams = TypedDict('WallapopCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

WallapopFilterOptionsDefaultParams = TypedDict('WallapopFilterOptionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'filter_id': Required[str],
    'category_id': Required[int],
    'brand': NotRequired[str],
    'q': NotRequired[str],
    'sort': NotRequired[Literal['closest', 'most_relevance', 'newest', 'price_low_to_high', 'price_high_to_low']],
    'options_query': NotRequired[str],
    'cursor': NotRequired[str],
}, total=False)

WallapopFilterOptionsTextResponseParams = TypedDict('WallapopFilterOptionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'filter_id': Required[str],
    'category_id': Required[int],
    'brand': NotRequired[str],
    'q': NotRequired[str],
    'sort': NotRequired[Literal['closest', 'most_relevance', 'newest', 'price_low_to_high', 'price_high_to_low']],
    'options_query': NotRequired[str],
    'cursor': NotRequired[str],
}, total=False)

WallapopFilterOptionsStreamParams = TypedDict('WallapopFilterOptionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'filter_id': Required[str],
    'category_id': Required[int],
    'brand': NotRequired[str],
    'q': NotRequired[str],
    'sort': NotRequired[Literal['closest', 'most_relevance', 'newest', 'price_low_to_high', 'price_high_to_low']],
    'options_query': NotRequired[str],
    'cursor': NotRequired[str],
}, total=False)

WallapopFiltersDefaultParams = TypedDict('WallapopFiltersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': NotRequired[str],
    'category_id': NotRequired[int],
}, total=False)

WallapopFiltersTextResponseParams = TypedDict('WallapopFiltersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': NotRequired[str],
    'category_id': NotRequired[int],
}, total=False)

WallapopFiltersStreamParams = TypedDict('WallapopFiltersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': NotRequired[str],
    'category_id': NotRequired[int],
}, total=False)

WallapopItemDetailDefaultParams = TypedDict('WallapopItemDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': Required[str],
}, total=False)

WallapopItemDetailTextResponseParams = TypedDict('WallapopItemDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': Required[str],
}, total=False)

WallapopItemDetailStreamParams = TypedDict('WallapopItemDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': Required[str],
}, total=False)

WallapopSearchDefaultParams = TypedDict('WallapopSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'latitude': Required[float],
    'longitude': Required[float],
    'category_id': NotRequired[int],
    'sort': NotRequired[Literal['closest', 'most_relevance', 'newest', 'price_low_to_high', 'price_high_to_low']],
    'min_price': NotRequired[float],
    'max_price': NotRequired[float],
    'condition': NotRequired[str],
    'is_shippable': NotRequired[Literal['true']],
    'time_filter': NotRequired[Literal['today', 'lastWeek', 'lastMonth']],
    'distance_in_km': NotRequired[int],
    'filter': NotRequired[list[str]],
    'cursor': NotRequired[str],
}, total=False)

WallapopSearchTextResponseParams = TypedDict('WallapopSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'latitude': Required[float],
    'longitude': Required[float],
    'category_id': NotRequired[int],
    'sort': NotRequired[Literal['closest', 'most_relevance', 'newest', 'price_low_to_high', 'price_high_to_low']],
    'min_price': NotRequired[float],
    'max_price': NotRequired[float],
    'condition': NotRequired[str],
    'is_shippable': NotRequired[Literal['true']],
    'time_filter': NotRequired[Literal['today', 'lastWeek', 'lastMonth']],
    'distance_in_km': NotRequired[int],
    'filter': NotRequired[list[str]],
    'cursor': NotRequired[str],
}, total=False)

WallapopSearchStreamParams = TypedDict('WallapopSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'latitude': Required[float],
    'longitude': Required[float],
    'category_id': NotRequired[int],
    'sort': NotRequired[Literal['closest', 'most_relevance', 'newest', 'price_low_to_high', 'price_high_to_low']],
    'min_price': NotRequired[float],
    'max_price': NotRequired[float],
    'condition': NotRequired[str],
    'is_shippable': NotRequired[Literal['true']],
    'time_filter': NotRequired[Literal['today', 'lastWeek', 'lastMonth']],
    'distance_in_km': NotRequired[int],
    'filter': NotRequired[list[str]],
    'cursor': NotRequired[str],
}, total=False)
