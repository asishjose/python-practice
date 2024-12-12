def sum_numbers(*values):
    total=0
    for i in values:
        total+=i
    print(total)
values=(12.5,3.147,98.1)
sum_numbers(*values)