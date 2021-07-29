from abc import ABC, abstractmethod

##############
# Interfaces #
##############

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temp: int, humidity: int, pressure: int):
        pass

# Display Element Interface
class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


# Subject Interface
class Subject(ABC):
    @abstractmethod
    def registerObserver(self, o: Observer):
        pass

    @abstractmethod
    def removeObserver(self, o: Observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass

##################
# Implementation #
##################

class WeatherData(Subject):
    def __init__(self):
        self._observers = []
        self._tempature = 0
        self._humidity = 0
        self._pressure = 0

    def registerObserver(self, o: Observer):
        self._observers.append(o)

    def removeObserver(self, o: Observer):
        self._observers.remove(o)

    def notifyObservers(self):
        for o in self._observers:
            o.update(temp=self._tempature, humid=self._humidity, pressure=self._pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temp: int, humidity: int, pressure: int):
        self._tempature = temp
        self._humidity = humidity
        self._pressure = pressure
        self.measurementsChanged()


class CurrentConditionDisplay(Observer, DisplayElement):
    def __init__(self, weatherData: WeatherData):
        self._tempature = 0
        self._humidity = 0
        self._pressure = 0
        self._weatherData = weatherData
        weatherData.registerObserver(self)

    def update(self, temp: int, humid: int, pressure: int):
        self._tempature = temp
        self._humidity = humid
        self._pressure = None
        self.display()

    def display(self):
        print("Current Conditions " + str(self._tempature) + "F " + str(self._humidity) + "%")

if __name__ == '__main__':
    weatherData = WeatherData()
    currentDisplay = CurrentConditionDisplay(weatherData)

    weatherData.setMeasurements(80, 65, 30.4)
    weatherData.setMeasurements(90, 61, 30.4)