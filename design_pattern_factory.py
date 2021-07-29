# Factory Design Pattern
# One of the most used design patterns, creational pattern.
# We create an obj w/o exposing creation logic to client and refer to
# the newly created object using a common interface.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("Inside rectangle draw method")

class Square(Shape):
    def draw(self):
        print("Inside sqaure draw method")

class ShapeFactory:
    def getShape(self, shapeType: str) -> Shape:
        if shapeType == None:
            return None
        elif shapeType == "Square":
            return Square()
        else:
            return Rectangle()

if __name__ == "__main__":
    shapeFactory = ShapeFactory()
    shape1 = shapeFactory.getShape("Square")
    shape1.draw()