from abc import ABC,abstractmethod
class Calculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass
    @abstractmethod
    def sub(self,a,b):
        pass
    @abstractmethod
    def mul(self,a,b):
        pass
    @abstractmethod
    def div(self,a,b):
        pass
class BasicCalculator(Calculator):
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

calc=BasicCalculator()
print('Addition: ',calc.add(10,5))
print('Substraction: ', calc.sub(10, 5))
print('Multiplication: ', calc.mul(10, 5))
print('Division: ', calc.div(10, 5))