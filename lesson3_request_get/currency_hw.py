import requests
import pandas as pd
from datetime import datetime, timedelta
from io import StringIO   

# Указываем первый и последний день искомой даты
start_date = datetime(2022, 2, 1)
end_date = datetime(2022, 2, 28)

# Генерируем все даты в табличку dates
dates = []
current_date = start_date
while current_date <= end_date:
    dates.append(current_date.strftime("%d/%m/%Y"))  # Формат: ДД/ММ/ГГГГ
    current_date += timedelta(days=1)

# Список для хранения данных
data = []

# Перебираем все даты
for date_str in dates:
    # Формируем URL для запроса к API Центробанка
    url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={date_str}"

    # Делаем запрос к API
    response = requests.get(url)
    response.encoding = 'windows-1251'  # Указываем правильную кодировку

    # Преобразуем строку XML в StringIO
    xml_data = StringIO(response.text)

    # Используем pandas для разбора XML
    df = pd.read_xml(xml_data, xpath=".//Valute[CharCode='USD']")  # Извлекаем только USD

    # Проверяем, есть ли данные о USD
    if not df.empty:
        usd_rate = df['Value'].iloc[0].replace(",", ".")  # Меняем запятую на точку
    else:
        usd_rate = "Нет данных"

    # Добавляем данные в список
    data.append([date_str, "USD", usd_rate])

# Создаем DataFrame
df_final = pd.DataFrame(data, columns=["date", "currency", "rub to usd"])

# Сохраняем данные в CSV без индекса
csv_filename = "usd_february_2022.csv"
df_final.to_csv(csv_filename, index=False, encoding="utf-8")

print(f"✅ Данные сохранены в {csv_filename}")

# Спрашиваем нужен ли вывод таблицы
table_input = input('Хотите вывести эту таблицу? "y" or "n": ' )
if table_input == 'y':
	df_read = pd.read_csv(csv_filename, index_col=False)
	print(df_read)
else:
	print('bb')
	
