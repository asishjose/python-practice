pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid = (l+u)//2
        if list[mid]==n:
            globals()['pos']=mid+1
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
list = [1,2,5,7,9,25,27,48,69]
n=69

if search(list,n):
    print('Found at ',pos)
else:
   print('Not found')

   #use for loop