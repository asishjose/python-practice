class Account:
    def __init__(self,name,account_number):
        self.__name=name
        self.__account_number=account_number
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, value):
        self.__account_number = value
if __name__=='__main__':
    account=Account('Asish',123456)
    print(account.name,account.account_number)
    account.name='John Doe'
    account.account_number=789000
    print(account.name, account.account_number)