from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print('its running')
class Whiteboard(Computer):
    def write(self):
        print('Its writing...')
class Programmer:
    def work(self,com):
        print('Solving Bugs')
        com.process
com1 = Laptop()
prog1=Programmer()
