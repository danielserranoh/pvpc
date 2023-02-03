
import requests
from requests.exceptions import HTTPError
import json

#auth_endpoint = "https://datadis.es/nikola-auth/tokens/login"

#hay que pasar estos dtos como variables que se cargan (datos de cliente?)
#token = "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1MDMxMjAwOVMiLCJhdXRob3JpdGllcyI6WyJQX0FVVE9SSVpBQ0lPTkVTIiwiUF9CVVNRX0lOVEVSIiwiUF9DT05TVUxfSU5GT19BR1JFR0FEIiwiUF9DT05TVU1fRElBX1NFTUFOQV9NRVMiLCJQX0RBVE9TX0NPTlRSQVRPIiwiUF9JTkZPUk1fUFJFREVGSU4iLCJQX01JU19TVU1JTklTVFJPUyIsIlBfTk9USUZJQ0FDIiwiUF9QT1RFTkNJQVMiLCJQX1NVTUlOSVNUUk9TX0FVVE9SIiwiUF9VU0VSIiwiUF9aT05BX1BSSVZBRF9HRVNUSU9OX0VTVEFEIl0sInB1YmxpY1VzZXIiOnsiaWQiOjE3NjMsIm5hbWUiOiJEYW5pZWwiLCJzdXJuYW1lIjoiU2VycmFubyIsImVtYWlsIjoiZGFuaWVsLnNlcnJhbm8uaEBnbWFpbC5jb20iLCJsb2dpbiI6IjUwMzEyMDA5UyIsImxhbmciOiJlcyIsImNvbXBsZXRlTmFtZSI6IkRhbmllbCBTZXJyYW5vIn0sImVudmlyb25tZW50IjoiUFJPIiwiaWF0IjoxNjc1MzgzNDU5LCJleHAiOjE2NzU0Njk4NTl9.b8c5PYXqyUt9BzOmdJcWFwNbzsm2udtL9sPMBPm8ezOVnFvBfP92kM5_RcYuxHbKriEaVkPW-nZ-AsRS8mo-_xbvUY-vGXCJmRhhxl1pGtj-SM2c0c_PQnHKw14I_MdeGYKRihYVar_hQ7PTHoqd6aw2qvaiBGxPP_jWWdnzDtPNQEC3svVni3o2giIFrV946JVZQeJIWqXs_JxDlm986EHYrq2opmUl4WkYwVtFGTSQKr6l1lPwEugVg6p9xbJB-Uq1XkSdo4-bMqc_hI5Y_JuViAD8z5pWecDbNPhiepyhfauK2zGyuMuc2VQTeXdk0cRTl8AUXTwHum8PtpLnXQ"
token = "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1MDMxMjAwOVMiLCJhdXRob3JpdGllcyI6WyJQX0FVVE9SSVpBQ0lPTkVTIiwiUF9CVVNRX0lOVEVSIiwiUF9DT05TVUxfSU5GT19BR1JFR0FEIiwiUF9DT05TVU1fRElBX1NFTUFOQV9NRVMiLCJQX0RBVE9TX0NPTlRSQVRPIiwiUF9JTkZPUk1fUFJFREVGSU4iLCJQX01JU19TVU1JTklTVFJPUyIsIlBfTk9USUZJQ0FDIiwiUF9QT1RFTkNJQVMiLCJQX1NVTUlOSVNUUk9TX0FVVE9SIiwiUF9VU0VSIiwiUF9aT05BX1BSSVZBRF9HRVNUSU9OX0VTVEFEIl0sInB1YmxpY1VzZXIiOnsiaWQiOjE3NjMsIm5hbWUiOiJEYW5pZWwiLCJzdXJuYW1lIjoiU2VycmFubyIsImVtYWlsIjoiZGFuaWVsLnNlcnJhbm8uaEBnbWFpbC5jb20iLCJsb2dpbiI6IjUwMzEyMDA5UyIsImxhbmciOiJlcyIsImNvbXBsZXRlTmFtZSI6IkRhbmllbCBTZXJyYW5vIn0sImVudmlyb25tZW50IjoiUFJPIiwiaWF0IjoxNjc1Mzc1MjcwLCJleHAiOjE2NzU0NjE2NzB9.cOrxnRJyQO-AytQjiSJY0WkKnoGqgvNRMEZoKZeZeM6qFLdbLiJc4aRhlptrtk5I6V95jMaAWCo3qmOzXikmiDUsdHUETc9vcQZq-S0GgByktRIgjVJfmSvDmCpantM222rcNfOlLuo0cw4RabBzP9rUs6ukHMXEks6ORFKbhOt0jwBP5eRKI0GjiWCLWLBoBqW-GqTioclKv1zBf-uBGA__I3lhAZUmfuIDTfgxHChqxzcLvmhcz8yEiSJCOY9xJ43DKYn1XGiyQw7cgImsoj622TjRS0QT3lZIer9x9UVV9LnuqfW57OWITSt5EnCmJipD1ofOwDIMXmto31hBnA"
cups = "ES0031105498058002SJ0F"
startDate="2022/09"
endDate="2022/12"
api_uri = "https://www.datadis.es/api-private/api/"


api_endpoint = 'get-consumption-data'
url = api_uri + api_endpoint
headers =  {"Authorization": f"Bearer {token}"}

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
    filename = "./data/cons_" + startDate.split("/")[0] + "-" + startDate.split("/")[1] + endDate.split("/")[1] + ".json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
