import pandas as pd

# Создаем список из словарей который считываем его  в датафрейме пандаса

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

df = pd.DataFrame(l_connection)
# print(df)
# print(type(df))

# Сохраняем данные с датафрейма в csv

df.to_csv('csv_sample.csv', index=False)

#считываем с csv в пандасе

df_read = pd.read_csv('csv_sample.csv')
print(df_read)
print(type(df_read))