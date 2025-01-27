import json
from typing import Dict, Any

def format_response_data(response_data: Dict[str, Any]) -> str:
    """
    Formats the response data into a human-readable string.
    
    Args:
        response_data (Dict[str, Any]): The raw response data from the API.
    
    Returns:
        str: A formatted string representation of the data.
    """
    if not response_data:
        return "No data available."
    
    formatted_data = []
    for key, value in response_data.items():
        formatted_data.append(f"{key}: {value}")
    
    return "\n".join(formatted_data)

def validate_input_data(data: Dict[str, Any]) -> bool:
    """
    Validates the input data for API requests.
    
    Args:
        data (Dict[str, Any]): The input data to validate.
    
    Returns:
        bool: True if the data is valid, False otherwise.
    """
    if not isinstance(data, dict):
        return False
    if "text" not in data or not isinstance(data["text"], str):
        return False
    if "chain" not in data or not isinstance(data["chain"], str):
        return False
    return True

def serialize_data(data: Dict[str, Any]) -> str:
    """
    Serializes the input data into a JSON string.
    
    Args:
        data (Dict[str, Any]): The input data to serialize.
    
    Returns:
        str: A JSON string representation of the data.
    """
    return json.dumps(data)

def deserialize_data(data: str) -> Dict[str, Any]:
    """
    Deserializes a JSON string into a Python dictionary.
    
    Args:
        data (str): The JSON string to deserialize.
    
    Returns:
        Dict[str, Any]: A Python dictionary representation of the data.
    """
    return json.loads(data)