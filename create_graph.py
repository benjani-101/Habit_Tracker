import requests
from config import PIXELA_USER_ENDPOINT, USERNAME, TOKEN, GRAPH_ID

graph_endpoint = f"{PIXELA_USER_ENDPOINT}/{USERNAME}/graphs"
graph_headers = {"X-USER-TOKEN": TOKEN}
graph_params = {
    "id": GRAPH_ID,
    "name": "reading_tracker",
    "unit": "pages",
    "type": "int",
    "color": "sora",
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_headers)
print(response.text)