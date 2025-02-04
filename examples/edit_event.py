"""
Example: Edit an Existing Event
"""
import os
from predx.agent.agent import Agent
from predx.agent.event_agent import EventAgent

private_key = os.getenv("PRIVATE_KEY")
if not private_key:
    raise ValueError("PRIVATE_KEY is not set. Please set it in your environment.")

agent = Agent(private_key)
print(f"Agent Address: {agent.get_agent_address()}")

auth_token = agent.gen_auth_token("SEIV2_TEST")
print(f"Auth Token: {auth_token}")

event_agent = EventAgent(private_key)


# Edit the event
response = event_agent.edit_event(
    bet_key="1711364298281CmOkv6u",
    bet_question="Will Shib surpass 10 million daily transactions by 2024 [TEST]?",
    bet_description="The question revolves around the potential growth of Shibarium...",
    category_list=["Crypto:Altcoin"],
    chain_name="SEIV2_TEST",
    expire_time="2025-01-25T17:00:00.000Z",
    image_url="https://pbs.twimg.com/media/Fl1XagYWQAIx7a-?format=jpg",
    language="ENGLISH",
    live_video_url="",
    trade_time="2024-03-27T04:00:00.000Z",
    auth_token=auth_token
)

print("✅ Edit Event Response:", response)
