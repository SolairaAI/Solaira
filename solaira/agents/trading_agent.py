from ..models import Response
from ..exceptions import InvalidAPIKeyError, RateLimitExceededError, BlockchainNotSupportedError

class TradingAgent:
    def __init__(self, client):
        self.client = client

    def place_order(self, symbol: str, side: str, amount: float, price: float) -> Response:
        """
        Places a trade order.
        
        Args:
            symbol (str): The trading pair (e.g., "SOL/USDC").
            side (str): The order side ("buy" or "sell").
            amount (float): The amount of the base token to trade.
            price (float): The price per unit of the base token.
        
        Returns:
            Response: The AI-generated response with order details.
        """
        response = self.client.call_endpoint(
            text=f"Place {side} order for {amount} {symbol} at {price}",
            chain="solana",
            deep_mode=True,
            max_tokens=500,
            temperature=0.7
        )
        return response

    def cancel_order(self, order_id: str) -> Response:
        """
        Cancels an existing order.
        
        Args:
            order_id (str): The ID of the order to cancel.
        
        Returns:
            Response: The AI-generated response with cancellation details.
        """
        response = self.client.call_endpoint(
            text=f"Cancel order with ID {order_id}",
            chain="solana",
            deep_mode=True,
            max_tokens=500,
            temperature=0.7
        )
        return response