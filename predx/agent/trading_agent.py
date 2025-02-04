from predx.agent.agent import Agent
from predx.utils.api import call_api
import traceback

class TradingAgent(Agent):
    def __init__(self, private_key, name="TradingAgent"):
        """
        Initializes the TradingAgent with private key and name
        
        :param private_key: A unique private key for the agent
        :param name: Name of the agent
        """
        super().__init__(private_key, name)
        self.event_type = "Trading"
        print(f"TradingAgent {self.name} with type {self.event_type} created.")
    
    def place_order(self, bet_key, chain_name, price, share, operation, order_mode, is_yes, discount_rate=0, auth_token=None):
        """
        Places a buy or sell order for a bet.

        :param bet_key: Unique identifier of the bet.
        :param chain_name: Blockchain network name (e.g., 'SEIV2_TEST').
        :param price: Price per share for the order.
        :param share: Number of shares to buy or sell.
        :param operation: Type of operation: 1 for buy, -1 for sell.
        :param order_mode: Type of order: 'Market' or 'Limit'.
        :param is_yes: Indicates if the order is for 'Yes' (1) or 'No' (0).
        :param discount_rate: Discount rate for PRDX tokens (default is 0).
        """
        api_name = "/api/orderBookBuyOrSellABet"
        if not auth_token:
            auth_token = self.gen_auth_token(chain_name)

        data = {
            "params": {
                "bet_key": bet_key,
                "chain_name": chain_name,
                "price": price,
                "share": share,
                "operation": operation,
                "order_mode": order_mode,
                "is_yes": is_yes,
                "discount_rate": discount_rate,
                "user_address": self.user_address
            }
        }

        response = call_api(api_name, auth_token, data)

        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                print("Response is not valid JSON.")
                traceback.print_exc()
                return None
        else:
            print(f"Failed to place order. Status code: {response.status_code}")
            print(response.text)
            return None

