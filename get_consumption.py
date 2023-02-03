
import requests
from requests.exceptions import HTTPError

#auth_endpoint = "https://datadis.es/nikola-auth/tokens/login"

#hay que pasar estos dtos como variables que se cargan (datos de cliente?)
token = "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1MDMxMjAwOVMiLCJhdXRob3JpdGllcyI6WyJQX0FVVE9SSVpBQ0lPTkVTIiwiUF9CVVNRX0lOVEVSIiwiUF9DT05TVUxfSU5GT19BR1JFR0FEIiwiUF9DT05TVU1fRElBX1NFTUFOQV9NRVMiLCJQX0RBVE9TX0NPTlRSQVRPIiwiUF9JTkZPUk1fUFJFREVGSU4iLCJQX01JU19TVU1JTklTVFJPUyIsIlBfTk9USUZJQ0FDIiwiUF9QT1RFTkNJQVMiLCJQX1NVTUlOSVNUUk9TX0FVVE9SIiwiUF9VU0VSIiwiUF9aT05BX1BSSVZBRF9HRVNUSU9OX0VTVEFEIl0sInB1YmxpY1VzZXIiOnsiaWQiOjE3NjMsIm5hbWUiOiJEYW5pZWwiLCJzdXJuYW1lIjoiU2VycmFubyIsImVtYWlsIjoiZGFuaWVsLnNlcnJhbm8uaEBnbWFpbC5jb20iLCJsb2dpbiI6IjUwMzEyMDA5UyIsImxhbmciOiJlcyIsImNvbXBsZXRlTmFtZSI6IkRhbmllbCBTZXJyYW5vIn0sImVudmlyb25tZW50IjoiUFJPIiwiaWF0IjoxNjc1Mzc1MjcwLCJleHAiOjE2NzU0NjE2NzB9.cOrxnRJyQO-AytQjiSJY0WkKnoGqgvNRMEZoKZeZeM6qFLdbLiJc4aRhlptrtk5I6V95jMaAWCo3qmOzXikmiDUsdHUETc9vcQZq-S0GgByktRIgjVJfmSvDmCpantM222rcNfOlLuo0cw4RabBzP9rUs6ukHMXEks6ORFKbhOt0jwBP5eRKI0GjiWCLWLBoBqW-GqTioclKv1zBf-uBGA__I3lhAZUmfuIDTfgxHChqxzcLvmhcz8yEiSJCOY9xJ43DKYn1XGiyQw7cgImsoj622TjRS0QT3lZIer9x9UVV9LnuqfW57OWITSt5EnCmJipD1ofOwDIMXmto31hBnA"
cups = "ES0031105498058002SJ0F"
startDate="2022/06"
endDate="2022/12"
api_uri = "https://www.datadis.es/api-private/"


api_endpoint = 'get-consumption-data'
url = api_uri + api_endpoint
headers =  {"Content-Type":"application/json", "Authorization": f"Bearer {token}"}

print(headers)

try:
    response = requests.get(
        url,
        headers=headers,
        params={
            'cups' : cups,
            'distributorCode': "2",
            'pointType': "5",
            'measurementType': "0",
            'startDate': startDate,
            'endDate': endDate,
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
    # Deberia corresponder el filename al rango de fechas en lugar de la fecha de muestra?
    #filename = "./data/" + now.strftime('%Y%m%d%H%M') + ".json"
    with open(filename, 'w', encoding='utf-8') as f:
        filename = "./data/cons_" + now.strftime('%Y%m%d%H%M') + ".json"
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
