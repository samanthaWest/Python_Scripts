from abc import ABC, abstractmethod
import random

class SupportTicket:
    _id: str
    _customer: str
    _issue: str

    def __init__(self, customer, issue):
        self._id = random.random()
        self._customer = customer
        self._issue = issue
    
    def print_ticket(self):
        print(self._id, self._customer, self._issue)

class ProcessingStrategy(ABC):
    @abstractmethod
    def process_ticket(self, data: list) -> list:
        pass

class FIFO(ProcessingStrategy):
    def process_ticket(self, data: list) -> list:
        return data.copy()

class FILO(ProcessingStrategy):
    def process_ticket(self, data: list) -> list:
       return (data.copy()).reverse()

class Random(ProcessingStrategy):
    def process_ticket(self, data: list) -> list:
        return random.shuffle(data.copy())

class CustomerSupport:

    def __init__(self):
        self._tickets = []

    def create_ticket(self, customer, issue):
        self._tickets.append(SupportTicket(customer,issue))
    
    def processing_tickets(self, strategy: ProcessingStrategy):
        strategy.process_ticket(self._tickets)
        for i in self._tickets:
            print(i.print_ticket())

if __name__ == '__main__':
    customer_supp = CustomerSupport()
    customer_supp.create_ticket("Sam", "Cant log in")
    customer_supp.create_ticket("Sama", "Cant log in")
    customer_supp.create_ticket("Saman", "Cant log in")
    customer_supp.processing_tickets(FIFO())
    customer_supp.processing_tickets(FILO())
    customer_supp.processing_tickets(Random())