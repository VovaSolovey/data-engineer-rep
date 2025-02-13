from utility.csv_writer import CsvWriter

# Пример данных
data = [
    {"City": "Moscow", "Temperature": 12.5, "Wind Speed": 3.6, "Conditions": "Clear", "Datetime": "2024-02-13 14:30:15"},
    {"City": "London", "Temperature": 8.3, "Wind Speed": 5.2, "Conditions": "Cloudy", "Datetime": "2024-02-13 14:35:00"}
]

# Создаем объект и записываем данные
csv_writer = CsvWriter()
csv_writer.set_dictionary(data)
csv_writer.write_to_csv("weather_data")