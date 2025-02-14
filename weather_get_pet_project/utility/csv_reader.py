import csv

class CsvReader:
    def __init__(self, filename):
        self.filename = filename

    def read_from_csv(self):
        """Чтение данных из CSV и возврат их в виде списка"""
        data_list = []
        try:
            with open(self.filename, mode='r', encoding="utf-8") as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    data_list.append(row)
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден.")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
        return data_list

    def print_csv_table(self):
        """Чтение и вывод данных из CSV файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)  # Просто выводим строку как список
        except Exception as e:
            print(f"Ошибка при чтении CSV файла: {e}")