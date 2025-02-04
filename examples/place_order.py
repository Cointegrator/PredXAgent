"""
Example: Place a Market Order (Buy)
"""
import os
from predx.agent.agent import Agent
from predx.agent.trading_agent import TradingAgent

# Ensure the private key is set in the environment
private_key = os.getenv("PRIVATE_KEY")
if not private_key:
    raise ValueError("PRIVATE_KEY is not set. Please set it in your environment.")

# Initialize the agent
agent = Agent(private_key)
print(f"Agent Address: {agent.get_agent_address()}")

# Generate authentication token
auth_token = agent.gen_auth_token("SEIV2_TEST")
print(f"Auth Token: {auth_token}")

# Initialize trading agent
trading_agent = TradingAgent(private_key)

# Place a buy order
response = trading_agent.place_order(
    bet_key="1711364298281CmOkv6u",
    chain_name="SEIV2_TEST",
    price=50,
    share=1,
    operation=1,  # Buy
    order_mode="Market",
    is_yes=1,  # Yes side
    discount_rate=0,
    auth_token=auth_token
)

print("✅ Order Response:", response)
