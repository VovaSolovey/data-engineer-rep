import requests
import pandas as pd


api_key = '1c0421e5602ef0c1802dc2c1e5706ad7'
curr = 'RUB,GBP,EUR'
start_date = '2007-09-01'
end_date = '2025-02-09'

URL = f"https://api.currencylayer.com/change?access_key={api_key}&currencies={curr}&start_date={start_date}&end_date={end_date}"
r = requests.get(URL)   
result = r.json()
# print(result)
# print(end='\n'*2)
# print(f"dollar in {start_date} = {result.get('quotes').get('USDRUB').get('start_rate')} rub") 
# print(f"dollar in {start_date} = {result.get('quotes').get('USDGBP').get('start_rate')} gpb") 
# print(f"dollar in {start_date} = {result.get('quotes').get('USDEUR').get('start_rate')} eur") 


df = pd.DataFrame(result)
# print(df)
# print(type(df))

# Сохраняем данные с датафрейма в csv

df.to_csv('currency_rate.csv', index=False)

#считываем с csv в пандасе

df_read = pd.read_csv('currency_rate.csv', index_col=False)

print(df_read)
print(type(df_read))

4. Получить курс рубля к доллару и евро к доллару за каждый день ноября 2023 года - и записать в 1 csv файл в 3 колонки:
Дата  Валюта  Курс к доллару