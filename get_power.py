
import requests
from requests.exceptions import HTTPError
import json
import os 
from dotenv import load_dotenv


load_dotenv()
token = os.environ.get('token')
cups = os.environ.get('cups')

# dates should be input params
startDate="2022/06"
endDate="2022/12"

api_uri = "https://www.datadis.es/api-private/api/"
api_endpoint = 'get-max-power'
url = api_uri + api_endpoint

try:
    response = requests.get(
        url,
        params={
            'cups' : cups,
            'distributorCode': "2",
            'startDate': startDate,
            'endDate': endDate,
            },
        headers={
            'Authorization': f"Bearer {token}",
            },
        )

    # If the response was successful, no Exception will be raised
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6
except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6
else:
    print('Success! API data retrieved')
    filename = "./data/power_" + startDate.split("/")[0] + "-" + startDate.split("/")[1] + endDate.split("/")[1] + ".json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
