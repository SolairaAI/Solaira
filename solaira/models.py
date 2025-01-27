from pydantic import BaseModel

class Response(BaseModel):
    """Response model for Solaira API calls."""
    data: str
    metadata: dict

    def __str__(self):
        return f"Response(data={self.data}, metadata={self.metadata})"