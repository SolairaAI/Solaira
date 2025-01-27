import asyncio
from solaira import SolairaAsync

async def main():
    """
    Main asynchronous function to interact with the Solaira API.
    This function initializes the SolairaAsync client, makes an API call
    with specified parameters, and processes the response.
    """
    # Replace "your_deepseek_api_key" with your actual API key
    api_key = "your_deepseek_api_key"

    # Initialize the Solaira async client
    api = SolairaAsync(api_key=api_key)

    try:
        # Call the API endpoint asynchronously with specified parameters
        response = await api.call_endpoint(
            text="Predict market trends for Solana",
            chain="solana",
            deep_mode=False,      # Set to True if you want more detailed insights
            max_tokens=500,       # Limit the number of tokens in the response
            temperature=0.7,      # Controls randomness; lower values = more deterministic
            stream=False          # Set to True for streaming responses if supported
        )

        # Check if the response is successful and print the data
        if response.success:
            print("Response Data:", response.data)
            print("Metadata:", response.metadata)
        else:
            print("Error:", response.error_message)
            print("Details:", response.error_details)

    except Exception as e:
        # Handle exceptions that might occur during the API call
        print("An error occurred:", str(e))

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())
