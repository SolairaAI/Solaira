class InvalidAPIKeyError(Exception):
    """Raised when an invalid API key is provided."""
    pass

class RateLimitExceededError(Exception):
    """Raised when the API rate limit is exceeded."""
    pass

class BlockchainNotSupportedError(Exception):
    """Raised when an unsupported blockchain is specified."""
    pass