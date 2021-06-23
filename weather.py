import requests
from datetime import datetime

Api_key = 'f610f6a45d589a5e68bda473100c141a'
location = input("Enter Your City :")

complite_url = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+Api_key
Api_link = requests.get(complite_url)
Api_data = Api_link.json()


temp_city = ((Api_data['main']['temp']) - 273.15)
weather_brod = Api_data['weather'][0]['description']
hmdt = Api_data['main']['humidity']
wind_speed = Api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_brod)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_speed ,'kmph')
