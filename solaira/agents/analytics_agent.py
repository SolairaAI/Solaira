from ..models import Response
from ..exceptions import InvalidAPIKeyError, RateLimitExceededError, BlockchainNotSupportedError

class AnalyticsAgent:
    def __init__(self, client):
        self.client = client

    def analyze_wallet(self, wallet_address: str) -> Response:
        """
        Analyzes wallet activity.
        
        Args:
            wallet_address (str): The wallet address to analyze.
        
        Returns:
            Response: The AI-generated response with analysis data.
        """
        response = self.client.call_endpoint(
            text=f"Analyze wallet activity for {wallet_address}",
            chain="solana",
            deep_mode=True,
            max_tokens=500,
            temperature=0.7
        )
        return response

    def predict_trends(self, symbol: str) -> Response:
        """
        Predicts market trends for a given trading pair.
        
        Args:
            symbol (str): The trading pair to analyze (e.g., "SOL/USDC").
        
        Returns:
            Response: The AI-generated response with trend predictions.
        """
        response = self.client.call_endpoint(
            text=f"Predict market trends for {symbol}",
            chain="solana",
            deep_mode=True,
            max_tokens=500,
            temperature=0.7
        )
        return response