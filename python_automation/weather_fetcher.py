import requests

API_KEY = 'fc9fb32659d39095a4bd6dd459908cfa'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input('Enter a city name: ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperatureInC = round(data['main']['temp'] - 273.15, 2)
    temperatureInF = round((temperatureInC * 9/5) + 32, 2)

    print('Weather: ', weather)
    print(f'Temperature: {temperatureInF}°F')
else:
    print('An error occurred.')
