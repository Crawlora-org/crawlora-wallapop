"""Typed Wallapop client for the Crawlora hosted API."""

from .platform import WallapopClient, AsyncWallapopClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = WallapopClient
AsyncClient = AsyncWallapopClient
__version__ = '0.1.1'
DISPLAY_NAME = 'Wallapop'
PLATFORM = 'wallapop'
CONTRACT_REVISION = 'sha256:1ca3efeec45964fec9b408035f3dc4fd245fe008c7acacb8cc66f484e926a996'

__all__ = [
    "WallapopClient", "AsyncWallapopClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
