list1 = ["Dog", "Cat", 2, 5, 2.45, 6, 6.56, 7, 97, 6.1, 899, "Lion", "Tiger"]

for i in list1:
    if str(i).isnumeric() and i>=6:
        print(i)