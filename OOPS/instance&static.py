class Car:

    wheels=5
    def __init__(self):
        self.mil = 10
        self.com = 'BMW'

c1=Car()
c2=Car()

c1.mil=8
c2.mil=6
c2.com='Porsche'
c2.wheels=4
Car.wheels=6

print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)