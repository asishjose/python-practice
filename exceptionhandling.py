a=5
b=0

print('Process begins')
try:
    print('Resource Opened')
    print(a/b)
    k=int(input('Enter a number: '))
    print(k)
except ZeroDivisionError as e:
    print('Error occured: ',e)
except ValueError as e:
    print('Error occured: ',e)
except Exception as e:
    print('Something went wrong: ',e)
finally:
    print('Resource closed.')
    print('Bye...')
