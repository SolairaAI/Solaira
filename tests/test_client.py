import unittest
from solaira import Solaira, SolairaAsync
import asyncio

class TestSolairaClient(unittest.TestCase):
    def setUp(self):
        self.api_key = "your_deepseek_api_key"
        self.sync_client = Solaira(api_key=self.api_key)
        self.async_client = SolairaAsync(api_key=self.api_key)

    def test_sync_call_endpoint(self):
        # Test synchronous client
        response = self.sync_client.call_endpoint(
            text="Test sync call",
            chain="solana",
            deep_mode=False,
            max_tokens=100,
            temperature=0.5,
            stream=False
        )
        self.assertIsNotNone(response.data)
        self.assertIsNotNone(response.metadata)

    async def test_async_call_endpoint(self):
        # Test asynchronous client
        response = await self.async_client.call_endpoint(
            text="Test async call",
            chain="solana",
            deep_mode=False,
            max_tokens=100,
            temperature=0.5,
            stream=False
        )
        self.assertIsNotNone(response.data)
        self.assertIsNotNone(response.metadata)

    def test_async_call_endpoint_wrapper(self):
        # Wrapper to run async test
        asyncio.run(self.test_async_call_endpoint())

if __name__ == "__main__":
    unittest.main()