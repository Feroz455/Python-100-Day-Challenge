import requests
from location import lat, lon, data,api_key
print(f'Latitude: {lat}, Longitude: {lon}')


OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_parems = {
    "lat":lat,
    "lon":lon,
    "appid":api_key
}

response = requests.get(OWN_Endpoint, params=weather_parems)
print(response.json())