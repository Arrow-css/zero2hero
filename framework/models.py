import requests


# localhost:8000/ru/get_btc_price_by_currency/USD
class BtcPrice:
    prices = {}
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    # Мы создаем объект и поле prices 
    # Принимает словарь цен btc
    def __init__(self):
        self.prices = self.get_data()

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
    
    def get_data(self):
        response = requests.get(self.url)
        api_data = response.json()

        return api_data
