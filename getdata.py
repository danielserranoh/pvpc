import requests
from datetime import datetime, timedelta

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



'''

now = datetime.now()

# end_time = now.isoformat(timespec='minutes')
end_time = now
#end_time_str = now.strftime('%Y%m%d%H%M')
#print(end_time_str)
#end_time_left=end_time.split('T')





# NOW
print("NOW date arguments are")
delta = timedelta(hours=1)
start_time = now - delta
## start_time = now.replace(hour=now.hour-1)
print(start_time)
print(end_time)

# TODAY
print("TODAY date arguments are")
start_time = now.replace(hour=0).replace(minute=00)
end_time = now.replace(hour=23).replace(minute=59)
print(start_time)
print(end_time)

# LASTDAY
print("LASTDAY date arguments are")
delta = timedelta(seconds=0)
if now.hour > 19 :
    # El dato el de mañana
    delta = timedelta(days=1)
start_deta = (now+delta).replace(hour=00).replace(minute=00)
end_time = (now+delta).replace(hour=23).replace(minute=59)
print(start_time)
print(end_time)

# WEEK
print("WEEK date arguments are")
delta = timedelta(weeks=1)
start_time = now - delta
print(start_time)
print(end_time)

# MONTH
print("MONTH date arguments are")
# El argumento puede ser 28, 29, 30 o 31 en funcion del mes y de si es año bisiento
#Por otro lado, el argumento puede ser el mes completo
delta = timedelta(days=30)
start_time = now - delta
print(start_time)
print(end_time)

api_url = "https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?"
url = (api_url + 'start_date=' + start_time.isoformat(timespec='minutes') + '&' + 'end_date='+end_time.isoformat(timespec='minutes') + '&time_trunc=hour')
#url = "https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?start_date=2023-01-01T00:00&end_date=2023-01-17T23:59&time_trunc=hour"
print(url)
# PRUEBAS CON FECHAS PARA APRENDER
#print("Pruebas con fechas")
fecha_hora_str = now.strftime('%Y%m%d%H%M')
now_iso = now.strftime('%Y-%m-%dT%H:%M')

#print(fecha_hora_str)
#print(now_iso)


#r = requests.get(url)
#print(r.text)