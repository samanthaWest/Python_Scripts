from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self) -> None:
        print("Shape: Rectangle")

class Circle(Shape):
    def draw(self) -> None:
        print("Shape: Circle 1")

class ShapeDecorator(Shape):
    _decoratedShape: Shape

    def ShapeDecorator(self, decoratedShape: Shape):
        self._decoratedShape = decoratedShape
    
    def draw(self):
        self._decoratedShape.draw()

class RedShapeDecorator(ShapeDecorator):

    def __init__(self, decorateShape: Shape):
        self._decoratedShape = decorateShape
    
    def draw(self):
        self._decoratedShape.draw()
        self.setRedBorder(self._decoratedShape)
    
    def setRedBorder(self, decoratedShape: Shape):
        print("Border is red 2")

if __name__ == '__main__':
    circle = Circle()
    redCircle = RedShapeDecorator(Circle())
    circle.draw()
    redCircle.draw()

