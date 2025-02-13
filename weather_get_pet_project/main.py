import csv
import time
from utility.yaml_reader import YamlReader
from utility.request_sender import RequestSender
from utility.csv_writer import CsvWriter
from utility.csv_reader import CsvReader

def print_csv_table(file_name):
    # Читаем и выводим данные из CSV
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)  # Просто выводим строку как список
    except Exception as e:
        print(f"Ошибка при чтении CSV файла: {e}")

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
    print("\nWeather data from CSV file:")
    print_csv_table("weather_forecast.csv")

if __name__ == "__main__":
    main()
