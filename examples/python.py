import os

from crawlora_wallapop import WallapopClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with WallapopClient(api_key=api_key) as client:
    filters = client.filters(q='bicycle')
    print('filters', filters)
    categories = client.categories()
    print('categories', categories)
