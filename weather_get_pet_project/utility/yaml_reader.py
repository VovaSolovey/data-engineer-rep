import yaml

class YamlReader:
    # Создаем пустой список, куда будем загружать города
    def __init__(self):
        self.data_list = []

    def read_from_yaml(self, file_path):
        # Читаем YAML файл и сохраняем список городов в атрибут
        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                self.data_list = yaml.safe_load(file).get("cities", [])
        except FileNotFoundError:
            # Специфическая ошибка, если файл не найден
            print(f'File named {str(file_path)} does not exist.')
        except yaml.YAMLError as e:
            # Обработка ошибок, если YAML файл поврежден или некорректен
            print(f'Error loading YAML file: {e}')
        except Exception as e:
            # Ловим все другие исключения
            print(f'An unexpected error occurred: {e}')

    def get_data_list(self):
        # Возвращаем список городов
        return self.data_list
