# Builder Pattern
# Building obj step by step independent of other objects

from abc import ABC, abstractmethod

class Packing(ABC):
    @abstractmethod
    def pack(self):
        pass

class Item(ABC):
    name = None
    packing = None
    price = None

# Packing in a Wrapper
class Wrapper(Packing):
    def pack(self):
        return "Wrapper"

# Packing in a Bottle
class Bottle(Packing):
    def pack(self):
        return "Bottle"

# Burger abstract class of item interface
class Burger(Item):
    @abstractmethod
    def packing(self):
        return Wrapper()

    @abstractmethod
    def price(self):
        pass

# Cold Drink abstract class of item interface
class ColdDrink(Item):
    @abstractmethod
    def packing(self):
        return Bottle()
    
    @abstractmethod
    def price(self):
        pass

# Concrete Classes

class VegBurger(Burger):
    def price(self):
        return 25
    
    def name(self):
        return "Veg Burger"

class ChickenBurger(Burger):
    def price(self):
        return 27
    
    def name(self):
        return "Chicken Burger"

class Coke(ColdDrink):
    def price(self):
        return 30

    def name(self):
        return "Coke"

class Pepsi(ColdDrink):
    def price(self):
        return 39

    def name(self):
        return "Pepsi"

# Meal Class

class Meal:
    _items = [Item]

    def addItem(self, item: Item):
        self._items.append(item)

    def getCost(self):
        cost = 0

        for item in self._items:
            cost += item.price
        
        return cost

    def showItems(self):

        for item in self._items:
            print(item.name)


if __name__ == "__main__":
    meal = Meal()
    meal.addItem(VegBurger())
    meal.addItem(Coke())
    

