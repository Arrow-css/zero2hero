import requests

# Получение данных из внешниго источика 
# Превращаем данные в структуру данных python
def get_data(url):
    response = requests.get(url)
    api_data = response.json()
    return api_data

# Ядерная бизнес логика
def btc_culculate(btc_count, rate):
    result_data = btc_count * rate
    return result_data


# Логика представления 
# Мы можем ответ выводить в консоль, отдавать по HTTP, записывать в файл
def print_result(btc_count , currancy , result):
    print(f" {btc_count} BTC в валюте : {currancy} стоит {result} {currancy}")


# Формируем переменные 
# Получение данных от клиента
# HTTP зарпос, данные переданыне при запуске скрипта, конфиграция и тд
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
my_currancy = ("USD", "EUR")
btc_count = 10

api_data = get_data(url)

# Набор бизнес логи, работающая по данным клинета   
for currancy in my_currancy:
    rate_str = api_data["bpi"][currancy]["rate"]

    rate_float =  float( rate_str.replace(",","") )
    
    # rate = get_rate(api_data, currancy)
    result = btc_culculate(btc_count, rate_float)

    print_result(btc_count , currancy , result)






# int() - целочисленные значения 
# float() - значение с плавающей точкой 124.49
# float("1234.4")
# float("1,234.4")
# >>> my_str = "Суп`ер `стр`ок`а"
# >>> print(my_str.replace("`",""))
# Супер строка


# my_list = ("Red", "Blue")
# my_dict = {
#     "Red" : "Красный",
#     "Blue": "Синий",
#     "Purple": "Фиолетовый",
# }

# for i in my_list:
#     print(my_dict[i])


#  api_data =  {
#     "time": { 
#         "updated":"Jun 2, 2022 15:02:00 UTC",
#         "updatedISO":"2022-06-02T15:02:00+00:00",
#         "updateduk":"Jun 2, 2022 at 16:02 BST"
#     },
#     "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
#     "chartName":"Bitcoin",
#     "bpi":{
#         "USD":{
#             "code":"USD",
#             "symbol":"&#36;",
#             "rate":"30,087.4695",
#             "description":"United States Dollar",
#             "rate_float":30087.4695
#          },
#         "GBP":{
#             "code":"GBP",
#             "symbol":"&pound;",
#             "rate":"24,097.7463",
#             "description":"British Pound Sterling",
#             "rate_float":24097.7463
#         },
#         "EUR":{
#             "code":"EUR",
#             "symbol":"&euro;",
#             "rate":"28,231.3735",
#             "description":"Euro",
#             "rate_float":28231.3735
#         }
#     }
# }