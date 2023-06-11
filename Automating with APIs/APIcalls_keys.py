import requests

baseUrl = 'api.openweathermap.org/data/2.5/forecast'

parameters = {'APPID': 'key-value', 'q': 'Paris, FR'}

response = requests.get(baseUrl, params = parameters)
print(response.content)
