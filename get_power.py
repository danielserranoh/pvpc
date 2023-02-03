
import requests
from requests.exceptions import HTTPError

#auth_endpoint = "https://datadis.es/nikola-auth/tokens/login"

#hay que pasar estos dtos como variables que se cargan (datos de cliente?)
token = "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1MDMxMjAwOVMiLCJhdXRob3JpdGllcyI6WyJQX0FVVE9SSVpBQ0lPTkVTIiwiUF9CVVNRX0lOVEVSIiwiUF9DT05TVUxfSU5GT19BR1JFR0FEIiwiUF9DT05TVU1fRElBX1NFTUFOQV9NRVMiLCJQX0RBVE9TX0NPTlRSQVRPIiwiUF9JTkZPUk1fUFJFREVGSU4iLCJQX01JU19TVU1JTklTVFJPUyIsIlBfTk9USUZJQ0FDIiwiUF9QT1RFTkNJQVMiLCJQX1NVTUlOSVNUUk9TX0FVVE9SIiwiUF9VU0VSIiwiUF9aT05BX1BSSVZBRF9HRVNUSU9OX0VTVEFEIl0sInB1YmxpY1VzZXIiOnsiaWQiOjE3NjMsIm5hbWUiOiJEYW5pZWwiLCJzdXJuYW1lIjoiU2VycmFubyIsImVtYWlsIjoiZGFuaWVsLnNlcnJhbm8uaEBnbWFpbC5jb20iLCJsb2dpbiI6IjUwMzEyMDA5UyIsImxhbmciOiJlcyIsImNvbXBsZXRlTmFtZSI6IkRhbmllbCBTZXJyYW5vIn0sImVudmlyb25tZW50IjoiUFJPIiwiaWF0IjoxNjc1MzgzNDU5LCJleHAiOjE2NzU0Njk4NTl9.b8c5PYXqyUt9BzOmdJcWFwNbzsm2udtL9sPMBPm8ezOVnFvBfP92kM5_RcYuxHbKriEaVkPW-nZ-AsRS8mo-_xbvUY-vGXCJmRhhxl1pGtj-SM2c0c_PQnHKw14I_MdeGYKRihYVar_hQ7PTHoqd6aw2qvaiBGxPP_jWWdnzDtPNQEC3svVni3o2giIFrV946JVZQeJIWqXs_JxDlm986EHYrq2opmUl4WkYwVtFGTSQKr6l1lPwEugVg6p9xbJB-Uq1XkSdo4-bMqc_hI5Y_JuViAD8z5pWecDbNPhiepyhfauK2zGyuMuc2VQTeXdk0cRTl8AUXTwHum8PtpLnXQ"

cookie = "JSESSIONID=57219861C1F200279B0136B7A52A64B5"
cups = "ES0031105498058002SJ0F"
startDate="2022/06"
endDate="2022/12"
api_uri = "https://www.datadis.es/api-private/"


api_endpoint = 'get-max-power'
url = api_uri + api_endpoint
headers =  {"Content-Type":"application/json",
            "Authorization": f"Bearer {token}",
            "Cookie": f"{cookie}"}


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
    # Deberia corresponder el filename al rango de fechas en lugar de la fecha de muestra?
    #filename = "./data/" + now.strftime('%Y%m%d%H%M') + ".json"
    with open(filename, 'w', encoding='utf-8') as f:
        filename = "./data/power_" + now.strftime('%Y%m%d%H%M') + ".json"
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
