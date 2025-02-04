"""
Example: Create a Prediction Market Event
"""
from predx.agent.agent import Agent
from predx.agent.event_agent import EventAgent
import os

# Load Private Key from Environment Variable for Security
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Use environment variable (recommended)
if not PRIVATE_KEY:
    raise ValueError("PRIVATE_KEY is not set. Please set it in your environment.")

# Initialize Agent
agent = Agent(PRIVATE_KEY)
print(f"Agent Address: {agent.get_agent_address()}")

auth_token = agent.gen_auth_token("SEIV2_TEST")
print(f"Auth Token: {auth_token}")

# Initialize the event agent
event_agent = EventAgent(PRIVATE_KEY)

# Call the API to create an event
response = event_agent.create_event(
    bet_question="This is a test event",
    bet_description="A description for the test event",
    category_list=["Crypto:Bitcoin"],
    image_url="https://example.com/image.png",
    trade_time="2025-01-27T07:10:45.893Z",
    expire_time="2025-02-13T08:00:00.000Z",
    pre_trade_yes_price=0.5,
    pre_trade_no_price=0.5,
    pre_trade_total_share=100000,
    taker_amount=10,
    taker_amount_var=0.3,
    pre_trade_creator_share=0,
    is_ai_generated=False,
    chain_name="SEIV2_TEST",
    language="ENGLISH",
    is_group=0,
    live_video_url="",
    group_options=[],
    auth_token=auth_token
)

print("✅ Event Creation Response:", response)

