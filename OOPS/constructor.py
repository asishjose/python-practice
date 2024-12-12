class A:
    def __init__(self):
        print('in A init')
    def feature1(self):
        pass
    def feature2(self):
        pass
class B(A):
    def __init__(self):
        print('in B init')
        super().__init__()
    def feature3(self):
        pass
    def feature4(self):
        pass
b1 = B()
