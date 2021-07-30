# Transportation Strategy Design Pattern
# define family of algorithms and encapsulate each one to make them interchangeable
# capture abstraction in interface, burying implementation details in derived classes

from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def transport(self, base_fare: int) -> int:
        pass

class CityBus(Strategy):
    def transport(self, base_fare: int) -> int:
        return base_fare * 4.50

class PersonalCar(Strategy):
    def transport(self, base_fare: int) -> int:
        return base_fare * 15.00

class Taxi(Strategy):
    def transport(self, base_fare: int) -> int:
        return base_fare * 50.00

class StrategyToAirport():

    def __init__(self, base_fare: int, transport: Strategy):
        self._base_fare = base_fare
        self._transport = transport
    
    def transport(self) -> None:
        print(self._transport.transport(self._base_fare))

if __name__ == "__main__":
    travel = StrategyToAirport(1.5, CityBus())
    travel.transport()

    travel2 = StrategyToAirport(2.5, Taxi())
    travel2.transport()

    travel3 = StrategyToAirport(5.6, PersonalCar())
    travel3.transport()