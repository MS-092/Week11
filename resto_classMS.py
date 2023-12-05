class FancyFood:
    # Initializer with 2 parameters
    # With 4 hidden attrributes inside of the constructor function

    item_counter = 0
    def __init__(self, food_name, amount_ordered):
        FancyFood.item_counter += 1
        self.__item_counter = FancyFood.item_number
        self.__food_name = food_name
        self.__amount_ordered = amount_ordered
        self.__standard_price = self.PriceList()
        self.__calculated_price = self.__calculate_price()

    def __calculate_price(self):
        return self.__amount_ordered * self.__standard_price

# PriceList as dictionary for getting into between the item names and the price of the items
    def PriceList(self):
        prices = {
            'Dry Cured Iberian Ham': 177.80,
            'Wagyu Steaks': 450.00,
            'Matsutake Mushrooms': 272.00,
            'Kopi Luwak Coffee': 306.50,
            'Moose Cheese': 487.20,
            'White Truffles': 3600.00,
            'Blue Fin Tuna': 3603.00,
            'Le Bonnotte Potatoes': 270.81
        }
        return prices.get(self.__food_name, 0.00)

    def getPrice_MS(self):
        return self.__calculate_price()

    def getName_MS(self):
        return self.__food_name

    def getAmount_MS(self):
        return self.__amount_ordered

    def getStandard_MS(self):
        return self.__standard_price

# Accessors method for class
    def __str__(self):
        return f"Item#{self.__item_counter}\nFood: {self.__food_name} \nAmount: {self.__amount_ordered} lbs\nStandard Price: ${self.__standard_price:.2f}\nCost: ${self.__calculated_price:.2f}\n"