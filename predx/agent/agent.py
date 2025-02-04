from eth_account import Account
from predx.utils.api import call_api
import predx.config as config
import traceback

class Agent:
    def __init__(self, private_key, name="MyAgent"):
        """
        Initializes the PredXAgent with a private key and name.
        
        :param private_key: A unique private key for the agent (used for secure identification)
        :param name: Name of the agent
        """
        self.__private_key = private_key  # Private key (encapsulated)

        account = Account.from_key(self.__private_key)
        self.user_address = account.address

        self.name = name
        print(f"PredXAgent {self.name} created with a private key (hidden).")
    
    def display_info(self):
        """
        Displays basic information about the agent.
        """
        print(f"Agent Name: {self.name}")
    
    def get_agent_address(self):
        """
        Provides a method to access the private key securely.
        """
    
        return self.user_address
    
    def gen_auth_token(self, chain_name):
        api_name = "/api/getAuthByPrivateKey"
        session_cookie = ""
        data = {
            "params": {
                "chain_name": chain_name,
                "private_key": self.__private_key
            }
        }
        response = call_api(api_name, session_cookie, data)

        if response.status_code == 200:
            # Parse the JSON response
            try:
                response_json = response.json()  # Convert the response to a dictionary (JSON)
                auth_session = response_json.get("auth_session")  # Use .get() to safely access the key
                if auth_session:
                    return auth_session
                else:
                    print("auth_session not found in the response.")
                    return None
            except ValueError:
                print("Response is not valid JSON.")
                traceback.print_exc()
                return None
        else:
            print(f"API request failed. Status code: {response.status_code}")
            traceback.print_exc()
            return None
    
    def get_token_balance(self, chain_name, auth_token=None):
        """
        Fetches the token balance of the user.
        """
        api_name = "/api/getTokenBalanceByAddress"
        data = {
            "params": {
                "chain_name": chain_name,
                "user_address": self.user_address
            }
        }
        response = call_api(api_name, auth_token, data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch token balance. Status code: {response.status_code}")
            return None
        
    def trigger_withdraw_usdc(self, chain_name, amount, auth_token=None):
        """
        Initiates a withdrawal of USDC.
        """
        api_name = "/api/triggerWithdrawUSDC"
        if not auth_token:
            auth_token = self.gen_auth_token(chain_name)
        data = {
            "params": {
                "chain_name": chain_name,
                "num_token": amount,
                "user_address": self.user_address
            }
        }
        response = call_api(api_name, auth_token, data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to trigger withdrawal. Status code: {response.status_code}")
            return None


