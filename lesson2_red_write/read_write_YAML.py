import yaml


# 1.Запись файла и чтение файла формата YAML
# Ямл хорошо подходит хранить какие то листы и конфиги

l_connection = [
	{
		"user_name" : "etl_user",
		"password" : "12345"
	},
	{
		"user_name" : "test_user",
		"password" : "332"
	},
]

# # создаем файл формата ямл чтобы занести туда список из словарей 
with open(r'write_connections.yaml', 'w') as file:
	doc = yaml.dump(l_connection, file)


# открываем файл откуда хотим считывать информациб, 
# затем заносим этот файл в переменную и используем метод ямл.лоад с параметрами путя(алиас file), и загрузчика yaml.FullLoader

with open(r'write_connections.yaml', 'r') as file:
	conn_dic = yaml.load(file, Loader=yaml.FullLoader)
	print(conn_dic)
	print(type(conn_dic))


