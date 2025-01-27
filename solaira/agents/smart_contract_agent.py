from ..models import Response
from ..exceptions import InvalidAPIKeyError, RateLimitExceededError, BlockchainNotSupportedError

class SmartContractAgent:
    def __init__(self, client):
        self.client = client

    def deploy_contract(self, contract_code: str, network: str = "solana") -> Response:
        """
        Deploys a smart contract.
        
        Args:
            contract_code (str): The code of the smart contract.
            network (str): The blockchain network (e.g., "solana").
        
        Returns:
            Response: The AI-generated response with deployment details.
        """
        response = self.client.call_endpoint(
            text=f"Deploy smart contract on {network} with code: {contract_code}",
            chain=network,
            deep_mode=True,
            max_tokens=500,
            temperature=0.7
        )
        return response

    def optimize_contract(self, contract_address: str) -> Response:
        """
        Provides optimization suggestions for a smart contract.
        
        Args:
            contract_address (str): The address of the contract to optimize.
        
        Returns:
            Response: The AI-generated response with optimization suggestions.
        """
        response = self.client.call_endpoint(
            text=f"Optimize smart contract at address {contract_address}",
            chain="solana",
            deep_mode=True,
            max_tokens=500,
            temperature=0.7
        )
        return response