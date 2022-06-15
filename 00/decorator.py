
import time

value_str = "текст"
value_int = 42

def speed_test(debug):

    def actual_decorator(func):
        if debug:
            print(f"Мы запустили {func.__name__}")

        def wrapper(*args):
            start_time = time.perf_counter_ns()

            # print(type(args))
            # value_1, value_2  = args
            # print(value_1, value_2)
            result = func(*args)
            if debug:
                print(f"{func.__name__} проработа {time.perf_counter_ns() - start_time} нано секунд ")

            # print(f"Результат работы  {func.__name__} будет {result}")
            
            return result
        
        return wrapper

    return  actual_decorator

# multiply = speed_test(multiply)
@speed_test(debug = 0)
def multiply(value_int, value_int_2):
    count = 5
    result = 0
    for i in range(100000):
        result += value_int * value_int_2
    return result

# division = big_func(division)
@speed_test(debug = 1)
def division(value_1, value_2, value_3):
    return value_1 / value_2 / value_3



print( multiply(12,12) )
print( division(12,12,14) )
# print(division(12, 12, 14))

# Как раньше
# Мы запустили multiply
# Результат работы  multiply будет 144
# 144
# Мы запустили division
# Результат работы  division будет 0.07142857142857142
# 0.07142857142857142

# Как сейчас 
# Мы запустили multiply
# Мы запустили division
# Результат работы  multiply будет 144
# 144
# Результат работы  division будет 0.07142857142857142
# 0.07142857142857142


# def func_1(*args, **asdasdsads):

#     print(args)
#     print(asdasdsads)





    # print(debug)

    # print(log_level)

# func_1(value_int, value_str, log_level="error")

# big_func(value_func)
# big_func(division)

# print(big_func.__name__)


# print(value_str)
# print(value_int)
# print(value_func)