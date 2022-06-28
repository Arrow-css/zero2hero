from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import json

import view

# path = "/ru/post/672434/"
def dispath(path:str)->list:
    path_list = path.split("/")

    # ['', 'ru', 'post', '672434', '']
    if len(path_list) < 3:
        return ["", "404 page", "1434"]

    lang_data = path_list[1] 
    action = path_list[2] 
    param = path_list[3].split(",")    
    return [lang_data, action, param]
    # print(path_list)

def render(result, error = ""):
    result_data = {
        "result" : result,
        "error" : error,
    }

    return json.dumps(result_data, ensure_ascii=False)

# localhost:8000/ru/post/672434/
# localhost:8000/ru/get_all_post/672434/
# localhost:8000/ru/prin_my_name/Aleksandr/
# localhost:8000/ru/prin_my_name/Vyacheslav/
# localhost:8000/ru/quad_number/15/

class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        lang_data, action, param = dispath(self.path)
        
        # print(view.action_dict)

        result:str = str()
        

        #
        #  {
        #  'post': {'action': <function post at 0x7ffbfba6ddc0>},
        #  'all_post': {'action': <function get_all_post at 0x7ffbfba6dee0>},
        #  'print_my_name': {'action': <function prin_my_name at 0x7ffbfb9d7040>}
        # }
        # action = "print_my_name"
        if view.action_dict.get(action):
            action_func = view.action_dict[action]["action"]
            result = action_func(*param)
        else:
            result = "404 page not found"
            

        # print(result)

        result_str = render(result)

        self.wfile.write(result_str.encode())

# localhost:8000/ru/post/672434/
# python3
# https:// - тип транспорта запрос - http, s - защищенный, шифрованный
# habr.com - домен, по адресу которого происходит обращение
# /ru - модификато языка
# /post - удаленная функция/метод данные которого мы хотим получить
# /672434 - это параметр, который мы передаем в нашу функцию/метод

# Слой транспорта 
    # - Разбирает http запрос 
    # - Понимает, какую функцию/метод нужно вызвать
    # - Вызвает его и передает параметры
    # - Получает результат работы удаленного метода
    # - Форматирует ответ, в нужный формат 
    # - Возвращает ответ на браузер

def run(server_class=HTTPServer, handler_class=HttpGetHandler):
  server_address = ('localhost', 8000)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()

run()