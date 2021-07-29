# Decorator Design Pattern

class Component():
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> str:
        return self._component

    def operation(self) -> str:
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"

def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")

if __name__ == "__main__":
    simple = ConcreteComponent()
    client_code(simple)
    decorator1 = ConcreteDecoratorA(simple)
    client_code(decorator1)
    decorator2 = ConcreteDecoratorA(decorator1)
    client_code(decorator2)