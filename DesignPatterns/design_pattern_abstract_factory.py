# Abstract Factory Method
# Factory of factories, interface for creating a factory or related objects
# without explicitly specifying their classes.

from abc import ABC, abstractmethod

def Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

def RoundedRectangle(Shape):
    def draw(self):
        print("Drawing Rounded Rectnagle")

def RoundedSquare(Shape):
    def draw(self):
        print("Drawing Rounded Square")

def Rectangle(Shape):
    def draw(self):
        print("Drawing Rectnagle")

def Square(Shape):
    def draw(self):
        print("Drawing Square")

def AbstractFactory(ABC):
    @abstractmethod
    def getShape(self, shapeType: str) -> Shape:
        pass

def ShapeFactory(AbstractFactory):
    def getShape(self, shapeType: str) -> Shape:
        if shapeType == "RECTANGLE":
            return Rectangle(self)
        if shapeType == "SQUARE":
            return Square(self)

        return None

def RoundedShapeFactory(AbstractFactory):
     def getShape(self, shapeType: str) -> Shape:
        if shapeType == "RECTANGLE":
            return RoundedRectangle(self)
        if shapeType == "SQUARE":
            return RoundedSquare(self)

class FactoryProducer:
    def getFactory(self, rounded: bool) -> AbstractFactory:
        if rounded:
            return RoundedShapeFactory(self)
        else:
            return ShapeFactory(self)

if __name__ == '__main__':
    shapeFactory = FactoryProducer()
    shapeFactory = shapeFactory.getFactory(False)
    shape1 = shapeFactory.getShape("SQUARE")
    shape1.draw()