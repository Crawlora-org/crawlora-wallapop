# crawlora-wallapop — Wallapop API client for Python

Python client for Crawlora's hosted Wallapop API. It exposes 5 API endpoints covering public listing search, categories, filters, and item details. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-python-homepage); the package does not run a browser or scrape
Wallapop locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Wallapop or its owners.

## Install

```sh
python -m pip install crawlora-wallapop
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_wallapop import WallapopClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with WallapopClient(api_key=api_key) as client:
    result_1 = client.filters(q='bicycle')
    print(result_1)
    result_2 = client.categories()
    print(result_2)
```

The package also exports `Client` as an alias for `WallapopClient`. Operation
methods are available directly in snake_case and through the `wallapop`
group. The async package client is `AsyncWallapopClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-wallapop/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-wallapop/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_wallapop import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.filters(q='bicycle')
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-wallapop/blob/main/examples/python.py) for a complete usage example.

## Supported Wallapop API endpoints

This package exposes every route below through direct snake_case methods and the `wallapop` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-wallapop/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/wallapop/categories` | `wallapop-categories` | Discover Wallapop search categories |
| `GET` | `/wallapop/filter-options` | `wallapop-filter-options` | Discover Wallapop remote filter values |
| `GET` | `/wallapop/filters` | `wallapop-filters` | Discover Wallapop search filters |
| `GET` | `/wallapop/item` | `wallapop-item-detail` | Fetch a public Wallapop listing detail page |
| `GET` | `/wallapop/search` | `wallapop-search` | Search Wallapop public listings |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
