f = open('mydata','r')
print(f)
#print(f.read())
print(f.readline(),end="")
# print(f.readline(4))

# f1 = open('mydata','w')
f2 = open('newdata','w')
f2.write('Something')
f3 = open('newdata','a')
f4 = open('newdata','r')
f3.write(' nothing!')
for data in f:
    f3.write(data)
print(f4.read())

#working with images
