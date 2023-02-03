

import requests
from requests.exceptions import HTTPError

auth_endpoint = "https://datadis.es/nikola-auth/tokens/login"

try:
    response = requests.post(
        auth_endpoint,
        params={
            'username' : "50312009S",
            'password': "akaneCh@n9",
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
    print(response.text)