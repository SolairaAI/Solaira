# API Reference 📚

This document provides detailed information about the Solaira API, including its clients, agents, and configuration options.

---

## Synchronous Client
The synchronous client is used for blocking operations.

### Class: `Solaira`
- **Initialization**:
  ```python
  from solaira import Solaira

  api = Solaira(api_key="your_deepseek_api_key")
  ```
  
### Method: call_endpoint
```
response = api.call_endpoint(
    text="Your input text",
    chain="solana",
    deep_mode=True,
    max_tokens=500,
    temperature=0.7,
    stream=False
)
```

### Parameters
- text: The input text for the AI (e.g., a query or command).
- chain: The blockchain to interact with (e.g., solana, ethereum).
- deep_mode: Enable deeper analysis (default: False).
- max_tokens: Control the length of the response (default: 500).
- temperature: Adjust the creativity of the AI's response (default: 0.7).
- stream: Enable streaming for real-time outputs (default: False).

### Returns
- A Response object containing:
	- data: The AI-generated response.
	- metadata: Additional information about the request (e.g., tokens used, response time).
	
## Agents 🤖
### Trading Agent
**Description:** Automates trading strategies on Solana.
**Methods:**
- place_order: Places a trade order.
```
response = api.trading_agent.place_order(
    symbol="SOL/USDC",
    side="buy",
    amount=10.0,
    price=25.0
)
```
### Parameters
- symbol: The trading pair (e.g., SOL/USDC).
- side: The order side (buy or sell).
- amount: The amount of the base token to trade.
- price: The price per unit of the base token.
- cancel_order: Cancels an existing order.
```
response = api.trading_agent.cancel_order(order_id="12345")
```
- order_id: The ID of the order to cancel.

## Smart Contract Agent
**Description:** Optimizes and automates smart contract interactions.
**Methods:**
- deploy_contract: Deploys a smart contract.
```
response = api.smart_contract_agent.deploy_contract(
    contract_code="...",
    network="solana"
)
```

### Parameters
- contract_code: The code of the smart contract.
- network: The blockchain network (e.g., solana).
- optimize_contract: Provides optimization suggestions.
```
response = api.smart_contract_agent.optimize_contract(contract_address="...")
```
- contract_address: The address of the contract to optimize.

## Analytics Agent
**Description:** Tracks wallet activity and market trends.
**Methods:** 
- analyze_wallet: Analyzes wallet activity.
```
response = api.analytics_agent.analyze_wallet(wallet_address="...")
```
### Parameters
- wallet_address: The wallet address to analyze.
- predict_trends: Predicts market trends.
```
response = api.analytics_agent.predict_trends(symbol="SOL/USDC")
```
- symbol: The trading pair to analyze (e.g., SOL/USDC).

## Configuration ⚙️
The Solaira API supports the following configuration options:
- api_key: Your DeepSeek AI API key.
- chain: Blockchain to interact with (e.g., solana, ethereum).
- deep_mode: Enable deeper analysis (default: False).
- max_tokens: Control the length of the response (default: 500).
- temperature: Adjust the creativity of the AI's response (default: 0.7).
- stream: Enable streaming for real-time outputs (default: False).

## Response Object
The Solaira API returns a Response object with the following attributes:
- data: The AI-generated response.
- metadata: Additional information about the request, including:
	- tokens_used: The number of tokens consumed.
	- response_time: The time taken to generate the response.
	- status: The status of the request (e.g., success, error).
	
## Error Handling
The Solaira API raises custom exceptions for easier debugging:
- InvalidAPIKeyError: Raised when an invalid API key is provided.
- RateLimitExceededError: Raised when the rate limit is exceeded.
- BlockchainNotSupportedError: Raised when an unsupported blockchain is specified.
