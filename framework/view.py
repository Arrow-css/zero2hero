import models


action_dict = dict()

# Про декотораторы
# Аутентификация/Авторизация

def rout(action_name):
    def actual_decorator(func):
        print(f"Наша функция {func.__name__} попала в декоратор" )
        
        action_dict[action_name] = {
            "action" : func,
        }

        def wrapper(*args):

            result = func(*args)
            return result

        return wrapper

    return actual_decorator


@rout("post")
def post(post_id):
    return f"post_id is {post_id}"

@rout("all_post")
def get_all_post(param):
    return "Все статьи на сгеодня"


# /ru/prin_my_name/Yevhen/ 
@rout("print_my_name")
def prin_my_name(name):
    return f"Добро пожаловать {name}"

# localhost:8000/ru/quad_number/15/

@rout("quad_number")
def quad_number(number):
    return f"Квадрат числа {number} будет равен {int(number) * int(number)}"



# localhost:8000/ru/get_btc_price_by_currency/USD
@rout("get_btc_price_by_currency")
def get_btc_price_by_currency(currency):
    btc_price_obj = models.BtcPrice()
    rate = btc_price_obj.get_rate_by_currancy("USD")
    return f"Стоимость Биткоина в валюте {currency} равна {rate}"

# localhost:8000/ru/how_many_btc_i_can_buy/USD,10000
@rout("how_many_btc_i_can_buy")
def how_many_btc_i_can_buy(currancy, money):
    btc_price_obj = models.BtcPrice()
    result = btc_price_obj.btc_from_money(currancy, int(money))
    return f"Вы можете купить  {result} биткоинов на сумму {money}{currancy}"


# Возвращает стоимость N btc в переданной валюте 
# localhost:8000/ru/multiply_btc_to_money/USD,9


# localhost:8000/ru/register/sasha,paswrd

@rout("register")
def registracion(login, password):
    return 