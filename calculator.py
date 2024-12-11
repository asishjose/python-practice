class Calculator:
    def addition(self,a,b):
        return a+b
    def substraction(self,a,b):
        return a-b
    def multipication(self,a,b):
        return a*b
    def division(self,a,b):
        return a/b

if __name__=="__main__":
    calc = Calculator()
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    operation=input('Enter operation to perform:(add,sub,mul,div): ')
    if operation=='add':
        result=calc.addition(num1,num2)
    elif operation=='sub':
        result=calc.substraction(num1,num2)
    elif operation=='mul':
        result=calc.multipication(num1,num2)
    else:
        result=calc.division(num1,num2)

    print(result)