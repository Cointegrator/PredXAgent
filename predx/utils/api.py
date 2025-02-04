import requests
import json
import predx.config as config

def call_api(api_name, session_cookie, data, method='POST'):
    """
    Calls an API with a dynamic endpoint, session cookie, and request data.

    :param api_name: The name of the API endpoint (e.g., '/api/createABet')
    :param session_cookie: The session cookie for authorization
    :param data: The data to be sent in the request (usually a dictionary)
    :param method: HTTP method (default is 'POST', can also use 'GET', 'PUT', etc.)
    :return: Response from the API request
    """
    # Base URL for your API (this can be updated depending on the environment)
    web_url = config.api_url
    url = web_url + api_name

    # Set the headers with the session cookie
    headers = {
        'Cookie': f'auth_session={session_cookie}',
        'Content-Type': 'application/json'
    }

    # Convert the data dictionary to JSON
    json_data = json.dumps(data)

    # Choose the request method dynamically (POST, GET, PUT, etc.)
    if method.upper() == 'POST':
        response = requests.post(url, headers=headers, data=json_data)
    elif method.upper() == 'GET':
        response = requests.get(url, headers=headers, params=data)
    elif method.upper() == 'PUT':
        response = requests.put(url, headers=headers, data=json_data)
    else:
        raise ValueError("Unsupported HTTP method. Use 'POST', 'GET', or 'PUT'.")

    # Return the response object for further processing
    return response

