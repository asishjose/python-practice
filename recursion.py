
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
x=10
result=fact(x)
print(result)