import requests
from .models import Response
from .exceptions import InvalidAPIKeyError, RateLimitExceededError, BlockchainNotSupportedError

class Solaira:
    def __init__(self, api_key: str):
        if not api_key:
            raise InvalidAPIKeyError("API key is required.")
        self.api_key = api_key
        self.base_url = "https://api.solaira.ai/v1"

    def call_endpoint(self, text: str, chain: str = "solana", deep_mode: bool = False, max_tokens: int = 500, temperature: float = 0.7, stream: bool = False) -> Response:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "text": text,
            "chain": chain,
            "deep_mode": deep_mode,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": stream,
        }

        response = requests.post(f"{self.base_url}/call", json=payload, headers=headers)
        if response.status_code == 401:
            raise InvalidAPIKeyError("Invalid API key.")
        if response.status_code == 429:
            raise RateLimitExceededError("Rate limit exceeded.")
        if response.status_code == 400:
            raise BlockchainNotSupportedError(f"Blockchain '{chain}' is not supported.")
        response_data = response.json()
        return Response(data=response_data.get("data"), metadata=response_data.get("metadata")) 