import csv
import time
from utility.yaml_reader import YamlReader
from utility.request_sender import RequestSender
from utility.csv_writer import CsvWriter
from utility.csv_reader import CsvReader

def main():
    # Чтение списка городов из YAML файла
    yaml_reader = YamlReader()
    yaml_reader.read_from_yaml("config/cities_for_forecast.yaml")
    cities = yaml_reader.get_data_list()

    # Получение данных о погоде для каждого города
    request_sender = RequestSender()
    weather_data = []

    for city in cities:
        weather = request_sender.get_weather_by_city(city)
        if weather:
            weather_data.append(weather)

        # Добавляем задержку 1 секунду между запросами
        time.sleep(1)

    # Запись данных в CSV файл
    csv_writer = CsvWriter()
    csv_writer.set_dictionary(weather_data)
    csv_writer.write_to_csv("weather_forecast")

    # Печатаем данные из CSV файла
    csv_reader = CsvReader('weather_forecast.csv')
    print("\nЧтение данных из CSV файла:")
    csv_reader.print_csv_table()  # Печать данных

if __name__ == "__main__":
    main()
