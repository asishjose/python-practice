class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand='hp'
            self.cpu='i3'
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1 = Student('Asish',2)
s2 = Student('Navin',4)

s1.show()
s2.show()
lap1 = Student.Laptop()