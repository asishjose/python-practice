#creating class
class Computer:
    def config(self):
        print('i5, 16gb, 1TB')

#creating object
com1 = Computer()
com2 = Computer()

#this is to just explain how it works
Computer.config(com1)
Computer.config(com2)

#common way
com1.config()
com2.config()
