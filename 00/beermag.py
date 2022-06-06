

class BeerMag:
    beer_price = {}
    store_name = ""

    # Создание объекта класса    
    # BeerMag(beer_price_06_06)
    # BeerMag.__init__(self, beer_price_06_06)
    def __init__(self, beer_price, store_name):
        self.store_name = store_name
        self.beer_price = beer_price

    def get_beer_price(self, beer_name):
        return self.beer_price[beer_name]
    
    def pritn_beer_price(self):
        print(self.beer_price)

    def print_price_jiguly(self):
        print(self.get_beer_price("Жигули"))

    def max_price_beer(self):
        low_price = {
            "beer_name" : "",
            "beer_price" : 0,
        }

        for i in self.beer_price:
            if low_price.get("beer_price", 0) < self.beer_price[i]:
                low_price["beer_name"] = i
                low_price["beer_price"] = self.beer_price[i]

        return low_price

    def print_max_price_beer(self):
        print(self.max_price_beer())
            

beer_price_06_06 = {
    "Жигули": 100,
    "Бад": 180,
    "Даф": 99,
    "Карона": 176,
}


beer_mag_obj = BeerMag(beer_price_06_06, "Пивзавод")
# beer_mag_obj.beer_price = beer_price_06_06
# print(beer_mag_obj.max_price_beer())
# print(beer_mag_obj.get_beer_price("Жигули"))


beer_mag_obj.print_max_price_beer()