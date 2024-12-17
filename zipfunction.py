names = ("Navin","Asish","Kiran")
comps = ("Dell","Apple","MS")

zipped = list(zip(names,comps))

print(zipped)

for (a,b) in zipped:
    print(a,b)