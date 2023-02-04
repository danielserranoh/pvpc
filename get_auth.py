

import requests
from requests.exceptions import HTTPError
import json
from dotenv import load_dotenv
import os 

load_dotenv()

token = os.environ.get('token')
auth_endpoint = "https://datadis.es/nikola-auth/tokens/login"

try:
    response = requests.post(
        auth_endpoint,
        params={
            'username' : os.environ.get('username'),
            'password': os.environ.get('password'),
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
    new_token = response.text
    #print(new_token)
    # Sustitur la cadena de texto correspondiente al token
    with open("./.env", "r+") as f:
        file = f.read()
    file = file.replace(token, new_token)
    with open("./.env", "w") as f:
         f.write(file)
        
    