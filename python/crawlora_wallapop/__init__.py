"""Typed Wallapop client for the Crawlora hosted API."""

from .platform import WallapopClient, AsyncWallapopClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = WallapopClient
AsyncClient = AsyncWallapopClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Wallapop'
PLATFORM = 'wallapop'
CONTRACT_REVISION = 'sha256:b02fd52a304c711998d8723a17adfd9b3eb7815d77f444a3f276679cf8ff4019'

__all__ = [
    "WallapopClient", "AsyncWallapopClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
