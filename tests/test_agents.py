import unittest
from solaira import Solaira

class TestSolairaAgents(unittest.TestCase):
    def setUp(self):
        self.api_key = "your_deepseek_api_key"
        self.client = Solaira(api_key=self.api_key)

    def test_trading_agent_place_order(self):
        # Test Trading Agent: place_order
        response = self.client.trading_agent.place_order(
            symbol="SOL/USDC",
            side="buy",
            amount=10.0,
            price=25.0
        )
        self.assertIsNotNone(response.data)
        self.assertIsNotNone(response.metadata)

    def test_smart_contract_agent_deploy_contract(self):
        # Test Smart Contract Agent: deploy_contract
        response = self.client.smart_contract_agent.deploy_contract(
            contract_code="...",
            network="solana"
        )
        self.assertIsNotNone(response.data)
        self.assertIsNotNone(response.metadata)

    def test_analytics_agent_analyze_wallet(self):
        # Test Analytics Agent: analyze_wallet
        response = self.client.analytics_agent.analyze_wallet(
            wallet_address="..."
        )
        self.assertIsNotNone(response.data)
        self.assertIsNotNone(response.metadata)

if __name__ == "__main__":
    unittest.main()