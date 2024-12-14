f1 = open('img.png','rb')
f2 = open('newimg.jpg','wb')

for i in f1:
    f2.write(i)

f3 = open('newimg.png','rb')
print(f3.read())