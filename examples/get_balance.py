"""
Example: Get Token Balance
"""
import os
from predx.agent.agent import Agent

# Ensure the private key is set in the environment
private_key = os.getenv("PRIVATE_KEY")
if not private_key:
    raise ValueError("PRIVATE_KEY is not set. Please set it in your environment.")

# Initialize the agent
agent = Agent(private_key)
print(f"Agent Address: {agent.get_agent_address()}")

# Define the chain name
chain_name = "SEIV2_TEST"

# Generate authentication token
auth_token = agent.gen_auth_token(chain_name)
print(f"Auth Token: {auth_token}")

# Fetch token balance
response = agent.get_token_balance(chain_name, auth_token)
print("✅ Token Balance Response:", response)
