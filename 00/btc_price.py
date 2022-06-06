import requests


class BtcPrice:
    prices = {}

    # Мы создаем объект и поле prices 
    # Принимает словарь цен btc
    def __init__(self, api_data):
        self.prices = api_data
    
    # Получаем rate в значении float по переданному в метод валюты
    # Принимает Валюту
    def get_rate_by_currancy(self, currancy):
        rate_str= self.prices["bpi"][currancy]["rate"]
        result  =  float( rate_str.replace(",","") )        
        return result

    # Считает, сколько стоит N Биткоинов в переданной валюте
    # Принимает кол-во битков и валюту
    def btc_calculate(self, btc_count, currancy):
        result = btc_count * self.get_rate_by_currancy(currancy)
        return result

    # Принимает валюту и кол-во денег, возвращает кол-во биткоинов, которых можно купить на эту сумму
    def btc_from_money(self, currancy, money):
        result = money / self.get_rate_by_currancy(currancy)
        return result
    
    # Принимаем на вход, стомтость биткоина, валюту, и возвращаем продать, 
    # если указанная нами стоимость выше стоимости 
    # Мы хотим продать btc если он будет стоить больше 30000 USD
    # Если он стоит выше 30 000 программа возвращает строку "Продать"
    # Если ниже, возвращает НЕ ПРОДАВАТЬ 
    
    def btc_sell(self, money_sell, currancy):
        if self.get_rate_by_currancy(currancy) > money_sell:
            return "Продать"
        else:
            return "Не продавать"

        # Всего денег 60000 USD
        # Биткоин стоит 30000 USD
        # Сколько мы купим Биткоинов
        # 60 000 / 30 000 = 2 

# Получение данных из внешниго источика 
# Превращаем данные в структуру данных python
def get_data(url):
    response = requests.get(url)
    api_data = response.json()
    return api_data

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
api_data = get_data(url)
btc_count = 8
money = 40000
quotation = [30000, 35000, 19900, 32000]

btc_price_obj = BtcPrice(api_data)
rate = btc_price_obj.get_rate_by_currancy("USD")
# result = btc_price_obj.btc_calculate(150, "USD")
result = btc_price_obj.btc_from_money("USD", money)
for i in quotation:
    action = btc_price_obj.btc_sell(i, "USD")
    print(action)


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