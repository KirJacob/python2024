# First, make an API call to https://jsonplaceholder.typicode.com/users to find the id for the user named "Ervin Howell".
# Using that id, make a second API call to https://jsonplaceholder.typicode.com/todos to get all the to-do items for that specific user.
# From that user's list of to-do items, count how many have the "completed" status set to true.
# Finally, assert or print a confirmation that the user has exactly 8 completed tasks.
# Include basic error handling in case the network requests fail.


import requests
import json

base_url = "https://jsonplaceholder.typicode.com"


def get_users():
    return requests.get(base_url + "/users")


def get_todos():
    return requests.get(base_url + "/todos")


def get_resp_dict():
    pass


#1
resp_users = json.loads(get_users().text)
user_to_find = "Ervin Howell"
filtered_user = list(filter(lambda user: user['name'] == user_to_find, resp_users))
result_01 = filtered_user_id = filtered_user[0]['id']
# print(result_01)


#2
# res = json.loads(get_users().text)get_todos()
print()
