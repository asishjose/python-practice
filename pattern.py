n=7
rows=4
for i in range(rows,0,-1):
    num=n
    for j in range(i):
        print(num,end=" ")
        num+=1
    n-=i-1
    print()