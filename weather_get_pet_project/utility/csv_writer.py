import csv

class CsvWriter:
    def __init__(self):
        self.data = []

    def set_dictionary(self, v_dictionaries):
        # Устанавливаем данные для записи в CSV
        self.data = v_dictionaries

    def write_to_csv(self, filename):
        # Записываем данные в CSV файл
        try:
            with open(filename + ".csv", mode='w', newline='', encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
                writer.writeheader()  # Записываем заголовки
                for row in self.data:
                    writer.writerow(row)  # Записываем строки данных
            print(f"Data successfully written to {filename}.csv")
        except Exception as e:
            print(f"Error writing to CSV file: {e}")