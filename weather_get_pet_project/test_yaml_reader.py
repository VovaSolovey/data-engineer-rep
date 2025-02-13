from utility.yaml_reader import YamlReader

yaml_reader = YamlReader()
yaml_reader.read_from_yaml("config/cities_for_forecast.yaml")  

print("Список городов:", yaml_reader.get_data_list())