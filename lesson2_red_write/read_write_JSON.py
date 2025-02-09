import json


# 1.Запись файла и чтение файла формата JSON

# json в массе своей применяется для перегона информации от бекенда к фронтэнду и наоборот

json_dic = {
		"user_name" : "etl_user",
		"password" : "12345",
		"user_lasname" : "usermanov",
		"kpi" : "0.2"
	}



# создаем строку из словарей с нужным форматирование индент 4 например
# Но важно понимать: json_obj — это просто строка, а не сам JSON-файл!

json_obj = json.dumps(json_dic, indent=4)

# без нее при записи возникнет ошибка так как метод .write принимает только строки
# пишем json

with open("sample.json", 'w') as json_out:
	json_out.write(json_obj)


# читаем JSON

with open("sample.json", 'r') as openfile:
	json_read = json.load(openfile)

print(json_read)
print(type(json_read))