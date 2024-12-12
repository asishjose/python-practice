class Home:
    def __init__(self):
        print('hey')
    def room1(self):
        print('This is Bedroom')
    def room2(self):
        print('This is Kitchen')
class FirstHome(Home):
    def room3(self):
        print('This is Work Area')
class SecondHome(Home):
    def room4(self):
        print('This is Study room')
home1=FirstHome()
home2=SecondHome()
home1.room1()
home1.room2()
home1.room3()