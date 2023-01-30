import requests
from requests.exceptions import HTTPError
from datetime import datetime, timedelta
import json

'''
IDEA: Montar un cli que también sea una API que permta recuperar 
Coger la fecha actual
Comprobar si con más o menos de las 20:00 CET españa, que es la hora a la que publican los nuevos datos del día siguente"

las peticiones deberían ser: 
.now = la ultima hora desde ahora (H -> H-1)
.today = Devuelve los datos de hoy mismo, independientemente de la hora
.lastday = devuelve el dato de hoy si antes de las 20 o el de mañana si después de las 20
.week = devuelve la ultima semana
.month = devuelve los datos del mes corriente delsde el día 1 del mes
.month(month_name) 
.days(X) = devuelve los X ultimos días desde hoy - tiene que parsear X


.lastfullweek = ultima semana completa
.lastfullmonth

# PRUEBAS CON FECHAS PARA APRENDER
#print("Pruebas con fechas")
#fecha_hora_str = now.strftime('%Y%m%d%H%M')
#now_iso = now.strftime('%Y-%m-%dT%H:%M')
'''

now = datetime.now()


# end_time = now.isoformat(timespec='minutes')
end_time = now
#end_time_str = now.strftime('%Y%m%d%H%M')
#print(end_time_str)
#end_time_left=end_time.split('T')





# NOW
print("\nNOW date arguments are")
delta = timedelta(hours=1)
start_time = now - delta
## start_time = now.replace(hour=now.hour-1)
#print(start_time)
#print(end_time)
print(" 🟢 " + start_time.strftime('%Y-%m-%dT%H:%M'))
print(" 🔴 " + end_time.strftime('%Y-%m-%dT%H:%M'))

# TODAY
print("\nTODAY date arguments are")
start_time = now.replace(hour=0).replace(minute=00)
end_time = now.replace(hour=23).replace(minute=59)
#print( start_time)
#print(end_time)
print(" 🟢 " + start_time.strftime('%Y-%m-%dT%H:%M'))
print(" 🔴 " + end_time.strftime('%Y-%m-%dT%H:%M'))

# WEEK
print("\nWEEK date arguments are")
delta = timedelta(weeks=1)
start_time = start_time - delta
#print(start_time)
#print(end_time)
print(" 🟢 " + start_time.strftime('%Y-%m-%dT%H:%M'))
print(" 🔴 " + end_time.strftime('%Y-%m-%dT%H:%M'))

# MONTH
print("\nMONTH date arguments are")
# El argumento puede ser 28, 29, 30 o 31 en funcion del mes y de si es año bisiento
#Por otro lado, el argumento puede ser el mes completo
delta = timedelta(days=30)
start_time = start_time - delta
#print(start_time)
#print(end_time)
print(" 🟢 " + start_time.strftime('%Y-%m-%dT%H:%M'))
print(" 🔴 " + end_time.strftime('%Y-%m-%dT%H:%M'))

# LASTDAY
print("\nLASTDAY date arguments are")
delta = timedelta(seconds=0)
if now.hour > 19 :
    # Pasadas las 20 horas está disponible el dato del día siguiente
    delta = timedelta(days=1)
start_time = (now+delta).replace(hour=00).replace(minute=00)
end_time = (now+delta).replace(hour=23).replace(minute=59)
#print(start_time)
#print(end_time)
print(" 🟢 " + start_time.strftime('%Y-%m-%dT%H:%M'))
print(" 🔴 " + end_time.strftime('%Y-%m-%dT%H:%M'))



api_endpoint = "https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?"
url = (api_endpoint + 'start_date=' + start_time.isoformat(timespec='minutes') + '&' + 'end_date='+end_time.isoformat(timespec='minutes') + '&time_trunc=hour')
#url = "https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?start_date=2023-01-01T00:00&end_date=2023-01-17T23:59&time_trunc=hour"
print("\n La url de llamada a la api es: " + url)




try:
    response = requests.get(
        api_endpoint,
        params={
            'start_date' : start_time.isoformat(timespec='minutes'),
            'end_date': end_time.isoformat(timespec='minutes'),
            'time_trunc': 'hour'
            },
        )

    # If the response was successful, no Exception will be raised
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6
except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6
else:
    print('Success!')
    # Deberia corresponder el filename al rango de fechas en lugar de la fecha de muestra?
    filename = "./data/" + now.strftime('%Y%m%d%H%M') + ".json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)



#pvpc = requests.get(url)
#print(pvpc.text)

