import requests
from config import PIXELA_USER_ENDPOINT, USERNAME, TOKEN, GRAPH_ID
from datetime import datetime

# format date in correct string format
date = datetime.now().strftime("%Y%m%d")


pixel_endpoint = f"{PIXELA_USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
pixel_headers = {"X-USER-TOKEN": TOKEN}

response = requests.delete(url=pixel_endpoint, headers=pixel_headers)
print(response.text)