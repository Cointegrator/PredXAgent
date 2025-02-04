"""
Example: Withdraw USDC Tokens
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

# Generate authentication token
chain_name = "SEIV2_TEST"
auth_token = agent.gen_auth_token(chain_name)
print(f"Auth Token: {auth_token}")

# Define withdrawal details
withdraw_amount = 0.1  # Example: Withdraw 0.1 USDC

# Trigger USDC withdrawal
response = agent.trigger_withdraw_usdc(chain_name, withdraw_amount, auth_token)
print("✅ Withdrawal Response:", response)
