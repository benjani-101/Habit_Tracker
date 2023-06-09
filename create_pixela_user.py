import requests
from config import PIXELA_USER_ENDPOINT, USERNAME, TOKEN

# POST request for creating user
user_endpoint = PIXELA_USER_ENDPOINT
user_params = {
    "token": TOKEN,  # self generated token (like API key but user defined)
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Post params as json. This post will create user
response = requests.post(url=user_endpoint, json=user_params)
print(response.text)