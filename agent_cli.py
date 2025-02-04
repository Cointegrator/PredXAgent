import argparse
from predx.agent.agent import Agent
from predx.agent.event_agent import EventAgent
from predx.agent.trading_agent import TradingAgent
from dotenv import load_dotenv
import predx.config as config
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description="PredX SDK CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    get_bet_brief_parser = subparsers.add_parser("get_bet_brief", help="Get brief information of a bet")
    get_bet_brief_parser.add_argument("private_key", help="Your private key")
    get_bet_brief_parser.add_argument("bet_key", help="Bet key to fetch")
    get_bet_brief_parser.add_argument("chain_name", help="Chain name")

    get_balance_parser = subparsers.add_parser("get_balance", help="Get token balance")
    get_balance_parser.add_argument("private_key", help="Your private key")
    get_balance_parser.add_argument("chain_name", help="Chain name")


    # Parse arguments
    args = parser.parse_args()

    if args.command == "get_bet_brief":
        private_key = args.private_key
        bet_key = args.bet_key
        chain_name = args.chain_name
        agent = EventAgent(private_key)
        auth_token = agent.gen_auth_token(chain_name)
        response = agent.get_bet_brief(bet_key, chain_name, auth_token)
        print("Response:", response)

    elif args.command == "get_balance":
        private_key = args.private_key
        chain_name = args.chain_name
        agent = Agent(private_key)
        auth_token = agent.gen_auth_token(chain_name)
        response = agent.get_token_balance(chain_name, auth_token)
        print("Response:", response)


if __name__ == "__main__":
    main()
