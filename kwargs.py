def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('asish',age=28,city='bangalore',mob=478465465)