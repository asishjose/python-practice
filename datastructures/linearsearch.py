pos=-1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i+1
            return True
        i+=1
    return False

list = [1,2,5,7,4,9]
n=9

if search(list,n):
    print('Found at ',pos)
else:
   print('Not found')

   #use for loop