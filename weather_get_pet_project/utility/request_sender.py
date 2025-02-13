import requests
from datetime import datetime
import os
import sys

sys.path.append("..")
from config.global_config import API_KEY

class RequestSender:
    def get_weather_by_city(self, city_name: str):
        api_key = API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&lang=ru&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            temperature = data.get('main', {}).get('temp', 'Undefined')
            wind_speed = data.get('wind', {}).get('speed', 'Undefined')
            conditions = data.get('weather', [{}])[0].get('main', 'Undefined')

            # Возвращаем данные в виде словаря
            date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            weather_data = {
                "City": city_name,
                "Temperature": temperature,
                "Wind Speed": wind_speed,
                "Conditions": conditions,
                "Datetime": date_time
            }
            return weather_data
        
        except requests.exceptions.RequestException as e:
            print(f"Error requesting weather data for {str(city_name)}: {e}")
            return None