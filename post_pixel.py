import requests
from config import PIXELA_USER_ENDPOINT, USERNAME, TOKEN, GRAPH_ID
from datetime import datetime

# format date in correct string format
date = datetime.now().strftime("%Y%m%d")


pixel_endpoint = f"{PIXELA_USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_headers = {"X-USER-TOKEN": TOKEN}
pixel_params = {
    "date": date,
    "quantity": input("How many pages did you read today?"),
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=pixel_headers)
print(response.text)