# f = open("Harshal.txt", "a")

# a = f.write("Harshal is GUJJU\n")
# print(a)
# f.close()

#Handle read and write both.

f = open("Harshal.txt", "r+")
print(f.read())

f.write("Jai mata di!")