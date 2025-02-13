import csv

class CsvReader:
    def __init__(self, filename):
        self.filename = filename

    def read_from_csv(self):
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