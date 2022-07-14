import requests
import time
import random, string



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


class Auth:
    db_file = "user.db"

    
    # vasya,123456;petya,654321;
    
    
    def register(self, login, password):
        user_data = ""

        # Открываем файл user.db на чтение
        with open(self.db_file, 'r') as f:
            users_data = f.read()
        
        user_list = users_data.split(";")

        # Смотрим, нет ли в файле такого же пользователя
        for user_data in user_list:
            # user_data = "vasya,123456"
            # user_data = "petya,654321"
            if not user_data:
                continue
            login_db, password_db = user_data.split(",")
            # login_db = "vasya"
            # password_db = "123456"

            print(f"логин = {login_db}, пароль = {password_db}")
            if login == login_db:
                return False
        
        # Открываем файл user.db на запись 
        with open(self.db_file, 'a') as f:
            # Записываем новую пару логин и пароль
            f.write(f"{login},{password};")
        return True



    def auth(self, login, password):
   
        """
        Принимет login и пароль, возращает True, если есть такой логин и пароль
        False, если совпадения не найдены.
        Смотрит, есть в базе данных такой логин и пароль 
        Если есть проверяет, возвращает True.
        Если нет возвращает False.
        """
    
        with open(self.db_file, 'r') as f:
            users_data = f.read()
        
        user_list = users_data.split(";")
        
        for user_data in user_list:

            if not user_data:
                continue
            login_db, password_db = user_data.split(",")

            if login == login_db and password == password_db:
                return True
            
        return False




class Session:
    db_file = "session.db"

    def create_session(self, login:str)->str:
        
        """
        Принимет login, возвращает session_id
        """

        session_id = self.rand_string(8)
        time_now  = time.time()

        with open(self.db_file, 'a') as f:
            f.write(f"{login},{session_id},{time_now};")
        return session_id
        
    def check_session(self, session_id:str)->str:
        """
        Принимет session_id, возвращает login
        Смотрит, есть в базе данных такой sesion_id 
        Если есть проверяет, что с момента записи не прошло более 5 минут.
        Если все условия выполнены, вовзращает login.
        """
        with open(self.db_file, 'r') as f:
            db_file = f.read()
        
        check_list = db_file.split(";")

        for session_string in check_list:
            # session_string = "login,session_id,time"
            if not session_string:
                continue

            login, current_session_id, create_time = session_string.split(",")
        
            if session_id == current_session_id:
                time_now  = time.time()     
                delta_time = time_now - float(create_time)           

                if delta_time < 60*5:
                    return login

    

    def rand_string(self,length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))



if __name__ == "__main__":
    auth = Auth()
    print(auth.register("login", "password"))

    print(auth.auth("login", "password"))
    # print(auth.register("vasya_1", "123456"))

    #session = Session()
    #login = "ALKSjdksaj"
    #session_id = session.create_session(login)
    # session_id = "brhburti"
    #print(session.check_session(session_id))

    