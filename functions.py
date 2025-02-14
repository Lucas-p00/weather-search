import requests

def get_weather_from_api(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric&lang=pt"
    response = requests.get(complete_url)
    return response.json()

def get_weather(city_name):
    api_key = "7a2445bfaf469533688264c7d6d17405"
    weather_data = get_weather_from_api(api_key, city_name)
    return weather_data
