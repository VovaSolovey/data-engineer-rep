from utility.request_sender import RequestSender

# Создаем объект класса
request_sender = RequestSender()

# Тестируем получение погоды для одного города
city = "Moscow"
weather_data = request_sender.get_weather_by_city(city)

# Выводим результат
print("Полученные данные о погоде:")
print(weather_data)