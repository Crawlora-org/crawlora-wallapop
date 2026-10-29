import os
import tempfile
import unittest
from pathlib import Path

from mypy import api

import crawlora_wallapop as client_package


TYPECHECK_SOURCE = '''
from typing_extensions import assert_type
from crawlora_wallapop import AsyncClient, AsyncWallapopClient, Client, WallapopClient
from crawlora_wallapop.platform import WallapopSearchResponse

def check_sync() -> None:
    named: WallapopClient = Client(api_key="key")
    with Client(api_key="key") as client:
        assert_type(client.search(category_id=7, latitude=7.5, longitude=7.5, q='test value'), WallapopSearchResponse)
        assert_type(client.search(_response_type='text', category_id=7, latitude=7.5, longitude=7.5, q='test value'), str)
        assert_type(client.search(_response_type='stream', category_id=7, latitude=7.5, longitude=7.5, q='test value').read(), bytes)
        assert_type(client.request('wallapop-search', {'category_id': 7, 'latitude': 7.5, 'longitude': 7.5, 'q': 'test value'}), WallapopSearchResponse)
        assert_type(client.wallapop.search(category_id=7, latitude=7.5, longitude=7.5, q='test value'), WallapopSearchResponse)
        assert_type(client.wallapop.search(_response_type='text', category_id=7, latitude=7.5, longitude=7.5, q='test value'), str)
        assert_type(client.wallapop.search(_response_type='stream', category_id=7, latitude=7.5, longitude=7.5, q='test value').read(), bytes)



async def check_async() -> None:
    named: AsyncWallapopClient = AsyncClient(api_key="key")
    async with AsyncClient(api_key="key") as client:
        assert_type(await client.search(category_id=7, latitude=7.5, longitude=7.5, q='test value'), WallapopSearchResponse)
        assert_type(await client.search(_response_type='text', category_id=7, latitude=7.5, longitude=7.5, q='test value'), str)
        assert_type((await client.search(_response_type='stream', category_id=7, latitude=7.5, longitude=7.5, q='test value')).read(), bytes)
        assert_type(await client.wallapop.search(category_id=7, latitude=7.5, longitude=7.5, q='test value'), WallapopSearchResponse)
        assert_type(await client.wallapop.search(_response_type='text', category_id=7, latitude=7.5, longitude=7.5, q='test value'), str)
        assert_type((await client.wallapop.search(_response_type='stream', category_id=7, latitude=7.5, longitude=7.5, q='test value')).read(), bytes)


'''

NEGATIVE_SOURCE = '''
from crawlora_wallapop import Client
Client().search(category_id=7, latitude=7.5, longitude=7.5, q=123)
Client().search()
'''


class PublicTypingTests(unittest.TestCase):
    def setUp(self):
        self.package_root = Path(client_package.__file__).resolve().parent
        self.old_mypy_path = os.environ.get("MYPYPATH")
        parent = str(self.package_root.parent)
        os.environ["MYPYPATH"] = parent if self.old_mypy_path is None else parent + os.pathsep + self.old_mypy_path

    def tearDown(self):
        if self.old_mypy_path is None:
            os.environ.pop("MYPYPATH", None)
        else:
            os.environ["MYPYPATH"] = self.old_mypy_path

    def test_installed_platform_stub_is_well_formed(self):
        stdout, stderr, status = api.run([
            "--strict", "--python-version=3.10", "--no-incremental", "--follow-imports=silent",
            str(self.package_root / "platform.pyi"),
        ])
        self.assertEqual(status, 0, stdout + stderr)

    def test_installed_client_signatures_accept_valid_calls_and_reject_invalid_calls(self):
        with tempfile.TemporaryDirectory(prefix="crawlora-python-mypy-") as temp:
            source_path = Path(temp) / "typecheck.py"
            source_path.write_text(TYPECHECK_SOURCE, encoding="utf-8")
            stdout, stderr, status = api.run([
                "--strict", "--python-version=3.10", "--no-incremental", "--follow-imports=silent", str(source_path),
            ])
        self.assertEqual(status, 0, stdout + stderr)

        with tempfile.TemporaryDirectory(prefix="crawlora-python-mypy-negative-") as temp:
            source_path = Path(temp) / "invalid.py"
            source_path.write_text(NEGATIVE_SOURCE, encoding="utf-8")
            stdout, stderr, status = api.run([
                "--strict", "--python-version=3.10", "--no-incremental", "--follow-imports=silent", str(source_path),
            ])
        self.assertNotEqual(status, 0, stdout + stderr)
        self.assertIn("q", stdout + stderr)


if __name__ == "__main__":
    unittest.main()
