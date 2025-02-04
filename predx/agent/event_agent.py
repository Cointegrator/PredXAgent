from predx.agent.agent import Agent
import traceback
from predx.utils.api import call_api

class EventAgent(Agent):
    def __init__(self, private_key, name="EventAgent"):
        """
        Initializes the EventAgent with private key and name
        
        :param private_key: A unique private key for the agent
        :param name: Name of the agent
        """
        super().__init__(private_key, name)
        self.event_type = "Event"
        print(f"EventAgent {self.name} with event type '{self.event_type}' created.")
    
    def create_event(self, bet_question, bet_description, category_list, image_url, trade_time, 
                 expire_time, pre_trade_yes_price, pre_trade_no_price, pre_trade_total_share, 
                 taker_amount, taker_amount_var, pre_trade_creator_share, is_ai_generated, 
                 chain_name, language, is_group, live_video_url, group_options, auth_token=None):
        """
        Creates a new prediction market event.

        :param bet_question: The main question for the bet.
        :param bet_description: A brief description of the bet.
        :param category_list: List of categories associated with the bet.
        :param image_url: URL of the event image.
        :param trade_time: Start time of trading (ISO 8601 format).
        :param expire_time: Expiration time of the event (ISO 8601 format).
        :param pre_trade_yes_price: Initial price for 'Yes' option.
        :param pre_trade_no_price: Initial price for 'No' option.
        :param pre_trade_total_share: Total shares available for the bet.
        :param taker_amount: Amount for taker participation.
        :param taker_amount_var: Variance for taker participation amount.
        :param pre_trade_creator_share: Shares allocated to the creator.
        :param is_ai_generated: Boolean indicating if the bet is AI-generated.
        :param chain_name: The blockchain network name.
        :param language: The language of the bet.
        :param is_group: Whether this is a group bet.
        :param live_video_url: URL for a live video related to the bet.
        :param group_options: Additional options for group bets.
        """
        api_name = "/api/createABet"
        if not auth_token:
            auth_token = self.gen_auth_token(chain_name)

        data = {
            "params": {
                "bet_question": bet_question,
                "bet_description": bet_description,
                "category_list": category_list,
                "image_url": image_url,
                "trade_time": trade_time,
                "expire_time": expire_time,
                "pre_trade_yes_price": pre_trade_yes_price,
                "pre_trade_no_price": pre_trade_no_price,
                "pre_trade_total_share": pre_trade_total_share,
                "taker_amount": taker_amount,
                "taker_amount_var": taker_amount_var,
                "pre_trade_creator_share": pre_trade_creator_share,
                "is_ai_generated": is_ai_generated,
                "chain_name": chain_name,
                "language": language,
                "is_group": is_group,
                "live_video_url": live_video_url,
                "group_options": group_options,
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
            print(f"API request failed. Status code: {response.status_code}")
            return None


    def edit_event(self, bet_key, bet_question, bet_description, category_list, chain_name, 
               expire_time, image_url, language, live_video_url, trade_time, auth_token=None):
        """
        Edits an existing prediction market event.

        :param bet_key: The unique identifier of the bet.
        :param bet_question: The main question for the bet.
        :param bet_description: A brief description of the bet.
        :param category_list: List of categories associated with the bet.
        :param chain_name: The blockchain network name.
        :param expire_time: Expiration time of the event (ISO 8601 format).
        :param image_url: URL of the event image.
        :param language: The language of the bet.
        :param live_video_url: URL for a live video related to the bet.
        :param trade_time: Start time of trading (ISO 8601 format).
        :param auth_token: Authentication token.
        """
        api_name = "/api/editABetByKey"
        if not auth_token:
            auth_token = self.gen_auth_token(chain_name)

        data = {
            "params": {
                "bet_key": bet_key,
                "bet_question": bet_question,
                "bet_description": bet_description,
                "category_list": category_list,
                "chain_name": chain_name,
                "expire_time": expire_time,
                "image_url": image_url,
                "language": language,
                "live_video_url": live_video_url,
                "trade_time": trade_time,
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
            print(f"API request failed. Status code: {response.status_code}")
            return None


        
    def fetch_all_bets_paged(
        self,
        chain_name,
        current_page,
        page_size,
        language="ENGLISH",
        sort_by="RELEVANT_ORDER",
        sort_direction="DEC",
        stage=["trading", "post-trading", "appeal"],
        ai_generated_events=None,
        parent_category="",
        child_category="",
        search_word="",
        user_address=None,
        auth_token=None
    ):
        """
        Fetches a paginated list of bets with optional filtering.

        :param chain_name: Blockchain network name.
        :param current_page: Current page number.
        :param page_size: Number of items per page.
        :param language: Language for the results (default: "ENGLISH").
        :param sort_by: Parameter to sort by (default: "RELEVANT_ORDER").
        :param sort_direction: Sort direction ("DEC" or "ASC", default: "DEC").
        :param stage: List of stages to filter bets.
        :param ai_generated_events: Filter for AI-generated events (True/False/None).
        :param parent_category: Parent category filter (default: "").
        :param child_category: Child category filter (default: "").
        :param search_word: Keyword search (default: "").
        :param user_address: User's address for personalized results (optional).
        """
        api_name = "/api/getAllBetsPaged"
        if not auth_token:
            auth_token = self.gen_auth_token(chain_name)

        data = {
            "params": {
                "chain_name": chain_name,
                "current_page": current_page,
                "page_size": page_size,
                "language": language,
                "sort_by": sort_by,
                "sort_direction": sort_direction,
                "stage": stage,
                "ai_generated_events": ai_generated_events,
                "parent_category": parent_category,
                "child_category": child_category,
                "search_word": search_word,
                "user_address": user_address
            }
        }

        response = call_api(api_name, auth_token, data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API request failed. Status code: {response.status_code}")
            return None

    def get_bet_brief(self, bet_key, chain_name, auth_token=None):
        """
        Fetches brief information of a specific bet using its key.
        """
        api_name = "/api/getBetByKeyBrief"
        data = {
            "params": {
                "bet_key": bet_key,
                "chain_name": chain_name
            }
        }
        response = call_api(api_name, auth_token, data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch bet brief. Status code: {response.status_code}")
            return None
