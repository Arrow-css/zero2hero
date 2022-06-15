class Human:
    name = str()
    age = int()
    home_adress = str()
    money = float()

    
    def __init__(self, name, age):
        self.name = name
        self.age = age 


    def can_buy_beer(self):
        if self.age < 18:
            return False
        else:
            return True 

    def eat(self, food):
        if food == "apple":
            print(f"{self.name} Съел яблоко") 
        elif food == "Поганки":
            print("Вызвать скорую помощь")
        else:
            print(f'Человек поел ябок')

class Children(Human):

    def eat(self, food):
        # self.can_buy_beer()
        if food == "apple":
            print(f"{self.name} Я не хочу есть яблоки, я хочу конфеты")
        else:
            super().eat(food)

class OldHUman(Human):
    pass 

fixture_data = {
    1 : {
        "name" : "Александр",
        "age" : 33,
    },
    2 : {
        "name" : "Филип",
        "age" : 24,
    },
    3 : {
        "name" : "Матвей",
        "age" : 5,
    },
}

food = "Поганки"
for i in fixture_data:
    if fixture_data[i]["age"] < 12:
        human = Children(fixture_data[i]["name"], fixture_data[i]["age"])
    else:
        human = Human(fixture_data[i]["name"], fixture_data[i]["age"])

    if human.can_buy_beer():
        print(f"{human.name} Может купить пива")
    else:
        print(f"{human.name} Не может купить пива")
    
    human.eat(food)