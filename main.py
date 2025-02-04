
from predx.agent.agent import Agent
from predx.agent.event_agent import EventAgent
from predx.agent.trading_agent import TradingAgent
from dotenv import load_dotenv
import predx.config as config
import os
import logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)


if __name__ == "__main__":
    load_dotenv()
    private_key = os.getenv("PRIVATE_KEY")

    # Creating an EventAgent
    agent = Agent(private_key)
    event_agent = EventAgent(private_key)
    trading_agent = TradingAgent(private_key)
    chain_name="BASE_MAIN"
    auth_token = event_agent.gen_auth_token(chain_name)
    # logging.info(auth_token)
    # response = event_agent.create_event({
    #             "bet_question": "agent event",
    #             "bet_description": "this is the description of the event",
    #             "category_list": [
    #                 "Crypto:Bitcoin"
    #             ],
    #             "image_url": "https://qph.cf2.quoracdn.net/main-qimg-1a4bafe2085452fdc55f646e3e31279c-lq",
    #             "activity_id": "",
    #             "trade_time": "2025-01-27T07:10:45.893Z",
    #             "expire_time": "2025-02-13T08:00:00.000Z",
    #             "pre_trade_yes_price": 0.5,
    #             "pre_trade_no_price": 0.5,
    #             "pre_trade_total_share": 100000,
    #             "taker_amount": 10,
    #             "taker_amount_var": 0.3,
    #             "pre_trade_creator_share": 0,
    #             "is_ai_generated": False,
    #             "chain_name": chain_name,
    #             "language": "ENGLISH",
    #             "is_group": 0,
    #             "live_video_url": "",
    #             "group_options": []
    #         }, auth_token)
    # logging.info(response)
    
    # # Get paged bets
    # response = event_agent.fetch_all_bets_paged(
    #     chain_name="BASE_MAIN",
    #     current_page=0,
    #     page_size=12,
    #     language="ENGLISH",
    #     sort_by="RELEVANT_ORDER",
    #     sort_direction="DEC",
    #     stage=["trading", "post-trading", "appeal"],
    #     ai_generated_events=False,
    #     parent_category="",
    #     child_category="",
    #     search_word="",
    #     user_address="0xc8B441106F482eF03D2E8ba1F244F2C598F8a471",
    #     auth_token=auth_token
    # )
    # print("Fetched Bets:", response)

    # # Get bet brief
    # bet_key = "-NrvH52e0g4ireC23UTK"  # Replace with the bet key you want to fetch
    # chain_name = "SEIV2_TEST"  # Replace with your chain name
    # bet_brief_response = event_agent.get_bet_brief(bet_key, chain_name)
    # print("Bet Brief Response:", bet_brief_response)

    # # Place a buy order
    # response = trading_agent.place_order(
    #     bet_key="-NrvH52e0g4ireC23UTK",
    #     chain_name="SEIV2_TEST",
    #     price=50,
    #     share=1,
    #     operation=1,  # Buy
    #     order_mode="Market",
    #     is_yes=1,  # Yes side
    #     discount_rate=0,
    #     auth_token=auth_token
    # )
    # print("Buy Order Response:", response)

    # # Place a sell order
    # response = trading_agent.place_order(
    #     bet_key="-NrvH52e0g4ireC23UTK",
    #     chain_name="SEIV2_TEST",
    #     price=50,
    #     share=1,
    #     operation=-1,  # Sell
    #     order_mode="Market",
    #     is_yes=1,  # Yes side
    #     discount_rate=0,
    #     auth_token=auth_token
    # )
    # print("Sell Order Response:", response)

    # # Get_token_balance
    # chain_name = "SEIV2_TEST"
    # balance_response = agent.get_token_balance(chain_name, auth_token)
    # print("Token Balance Response:", balance_response)

    # # Trigger_withdraw_usdc
    # withdrawal_amount = 0.1 
    # chain_name = "SEIV2_TEST"
    # withdrawal_response = agent.trigger_withdraw_usdc(chain_name, withdrawal_amount, auth_token)
    # print("Withdrawal Response:", withdrawal_response)