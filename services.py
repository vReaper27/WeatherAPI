import requests
import os


def fetch_weather_data(city):
    API_KEY = os.getenv('API_KEY')
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no'

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return {
        'city': data['location']['name'],
        'region': data['location']['region'],
        'country': data['location']['country'],
        'temperature': data['current']['temp_c'],
        'humidity': data['current']['humidity'],
        'wind_kph': data['current']['wind_kph'],
        'description': data['current']['condition']['text'],
        'last_updated': data['current']['last_updated']
    }
