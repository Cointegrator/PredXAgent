import argparse
import logging
import os
import json
from predx.agent.agent import Agent
from predx.agent.event_agent import EventAgent
from predx.agent.trading_agent import TradingAgent

# Configure logging
logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser(description="PredX SDK CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available Commands")

    # 🏆 Get Bet Brief
    get_bet_brief_parser = subparsers.add_parser("get_bet_brief", help="Get brief information of a bet")
    get_bet_brief_parser.add_argument("bet_key", help="Bet key to fetch")
    get_bet_brief_parser.add_argument("chain_name", help="Chain name")

    # 💰 Get Token Balance
    get_balance_parser = subparsers.add_parser("get_balance", help="Get token balance")
    get_balance_parser.add_argument("chain_name", help="Chain name")

    # 🎯 Place an Order
    place_order_parser = subparsers.add_parser("place_order", help="Place a trade order")
    place_order_parser.add_argument("bet_key", help="Bet key")
    place_order_parser.add_argument("chain_name", help="Chain name")
    place_order_parser.add_argument("price", type=float, help="Price per share")
    place_order_parser.add_argument("share", type=int, help="Number of shares")
    place_order_parser.add_argument("operation", type=int, choices=[1, -1], help="1=Buy, -1=Sell")
    place_order_parser.add_argument("order_mode", choices=["Market", "Limit"], help="Market or Limit order")
    place_order_parser.add_argument("is_yes", type=int, choices=[0, 1], help="1=Yes, 0=No")
    place_order_parser.add_argument("--discount_rate", type=float, default=0, help="Discount rate (optional)")

    # 🎭 Create an Event
    create_event_parser = subparsers.add_parser("create_event", help="Create a prediction event")
    create_event_parser.add_argument("bet_question", help="Bet question")
    create_event_parser.add_argument("bet_description", help="Description")
    create_event_parser.add_argument("category_list", nargs="+", help="List of categories")
    create_event_parser.add_argument("chain_name", help="Chain name")
    create_event_parser.add_argument("trade_time", help="Trade start time (ISO format)")
    create_event_parser.add_argument("expire_time", help="Expire time (ISO format)")
    create_event_parser.add_argument("pre_trade_yes_price", type=float, help="Initial Yes price")
    create_event_parser.add_argument("pre_trade_no_price", type=float, help="Initial No price")
    create_event_parser.add_argument("pre_trade_total_share", type=int, help="Total shares")
    create_event_parser.add_argument("taker_amount", type=float, help="Taker amount")
    create_event_parser.add_argument("taker_amount_var", type=float, help="Taker amount variance")
    create_event_parser.add_argument("--pre_trade_creator_share", type=int, default=0, help="Shares for creator")
    create_event_parser.add_argument("--is_ai_generated", type=bool, default=False, help="AI-generated event?")
    create_event_parser.add_argument("--language", default="ENGLISH", help="Language")
    create_event_parser.add_argument("--is_group", type=int, default=0, help="Group bet?")
    create_event_parser.add_argument("--live_video_url", default="", help="Live video URL")
    create_event_parser.add_argument("--image_url", default="", help="Event image URL")
    create_event_parser.add_argument("--group_options", nargs="*", help="Group options")

    # 🔄 Withdraw USDC
    withdraw_parser = subparsers.add_parser("withdraw", help="Withdraw USDC")
    withdraw_parser.add_argument("chain_name", help="Chain name")
    withdraw_parser.add_argument("amount", type=float, help="Amount to withdraw")

    # 🏁 Parse arguments
    args = parser.parse_args()

    # 🔑 Load private key from ENV
    private_key = os.getenv("PRIVATE_KEY")
    if not private_key:
        print("❌ PRIVATE_KEY is not set! Use 'export PRIVATE_KEY=your_key_here'")
        return

    # 🎯 Command Execution
    if args.command == "get_bet_brief":
        agent = EventAgent(private_key)
        auth_token = agent.gen_auth_token(args.chain_name)
        response = agent.get_bet_brief(args.bet_key, args.chain_name, auth_token)

    elif args.command == "get_balance":
        agent = Agent(private_key)
        auth_token = agent.gen_auth_token(args.chain_name)
        response = agent.get_token_balance(args.chain_name, auth_token)

    elif args.command == "place_order":
        agent = TradingAgent(private_key)
        auth_token = agent.gen_auth_token(args.chain_name)
        response = agent.place_order(
            args.bet_key, args.chain_name, args.price, args.share,
            args.operation, args.order_mode, args.is_yes, args.discount_rate, auth_token
        )

    elif args.command == "create_event":
        agent = EventAgent(private_key)
        auth_token = agent.gen_auth_token(args.chain_name)
        response = agent.create_event(
            args.bet_question, args.bet_description, args.category_list, args.image_url,
            args.trade_time, args.expire_time, args.pre_trade_yes_price, args.pre_trade_no_price,
            args.pre_trade_total_share, args.taker_amount, args.taker_amount_var,
            args.pre_trade_creator_share, args.is_ai_generated, args.chain_name,
            args.language, args.is_group, args.live_video_url, args.group_options, auth_token
        )

    elif args.command == "withdraw":
        agent = Agent(private_key)
        auth_token = agent.gen_auth_token(args.chain_name)
        response = agent.trigger_withdraw_usdc(args.chain_name, args.amount, auth_token)

    else:
        parser.print_help()
        return

    # ✅ Print structured JSON response
    print(json.dumps(response, indent=4))


if __name__ == "__main__":
    main()

