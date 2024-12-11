def decorator_fun(func):
    def wrapper():
        print('Hello World')
        func()
    return wrapper

@decorator_fun
def hello():
    print()
    # nothing printing here

hello()