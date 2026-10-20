# app.py
import requests as Requests
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

""" Global variables """

# The URL of the upstreams API.
api_url = "https://dummyjson.com/users"

# List of all user fields this API will return per user
user_fields = ["id","firstName","lastName","email","phone"]

# List of all user fields that we want to be filterable
user_fields_filterable = ["firstName","lastName"]

""" Main function """
@app.get("/users")
def get_users():    
    """ Handle request parameters """
    # user_filters contains all the fields that users will be filtered by.
    user_filters = {}
    for field in user_fields_filterable:
        # Check if the customer has included a query parameter, and add it
        # to user_filters if so.
        if (field in request.args):
            user_filters[field] = request.args[field]

    """ Communicate with the upstream API and obtain all users """

    try:
        # Setting the 'limit' param to 0 will retrieve all users from the upstreams API.
        response = Requests.get(api_url + "?limit=0")
    except Exception as err:
        abort(500, f"{err}")
        
    try:
        response.raise_for_status()
    except Exception as err:
        abort(response.status_code, f"{err}")

    # Convert response to json for easier handling
    try:
        response_json = response.json()
    except Exception as err:
        abort(500, f"{err}")
        

    """ Format the response and remove filtered """
    
    # Contains all users before filtering and formatting
    all_users = response_json["users"]
    
    # Contains all users after being filtered and formatted
    users = []
    
    for user in all_users:
        # First, check if user should be filtered
        filtered = False
        for field in user_filters:
            # If the user does not have the relevant field, don't include user.
            if (not field in user):
                filtered = True
                break
            # If the user field does not match the filter, don't include the user.
            if (user[field].lower() != user_filters[field].lower()):
                filtered = True
                break
        # If the user has been filtered, continue to next user without adding them.
        if (filtered):
            continue

        # Then, format the user and add it to users.
        user_formatted = {}
        for field in user_fields:
            # If user has the field, add it to user_formatted
            if (field in user):
                user_formatted[field] = user[field]
        users.append(user_formatted)

    # Transform the response and send it.
    response_transformed = {
        "total" : len(all_users),
        "count" : len(users),
        "users" : users
    }
    return jsonify(response_transformed)
