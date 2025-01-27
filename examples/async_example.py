import asyncio
from solaira import SolairaAsync

async def main():
    # Initialize the Solaira async client
    api = SolairaAsync(api_key="your_deepseek_api_key")

    # Call the API endpoint asynchronously
    response = await api.call_endpoint(
        text="Predict market trends for Solana",
        chain="solana",
        deep_mode=False,
        max_tokens=500,
        temperature=0.7,
        stream=False
    )

    # Print the response
    print("Response Data:", response.data)
    print("Metadata:", response.metadata)

# Run the async function
asyncio.run(main())