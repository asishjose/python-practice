class Computer:
    def __init__(self):
        self.name = 'Asish'
        self.age = 22

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
c1 = Computer()
c1.age = 29
c2 = Computer()

if c1.compare(c2):
    print('They are the same')
else:
    print('They are different')

print(c1.age)
print(c2.age)