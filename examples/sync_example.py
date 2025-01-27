from solaira import Solaira

# Initialize the Solaira client
api = Solaira(api_key="your_deepseek_api_key")

# Call the API endpoint synchronously
response = api.call_endpoint(
    text="Analyze Solana wallet activity",
    chain="solana",
    deep_mode=True,
    max_tokens=500,
    temperature=0.7,
    stream=False
)

# Print the response
print("Response Data:", response.data)
print("Metadata:", response.metadata)