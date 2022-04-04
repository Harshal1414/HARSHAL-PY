# faulty calculator

print("Type your operator: \n",
 "Type + for addition \n",
 "Type - for substraction \n",
 "Type / for division \n",
 "Type * fro mulitipication")

 #Taking input
type_cal=input("OPERATOR = ")

a='+'
b='-'
c='*'
d='/'

print("Enter the first number: ")
A = int(input("NUM 1 = "))
print("Enter the second number: ")
B = int(input("NUM 2 = "))

if type_cal == a:
    #for addition
    if (A == 56 and B == 9):
        print(77)
    else:
        print(A + B)
elif type_cal == b:
    print(A - B)
elif type_cal == c:
    if (A == 45 and B == 9):
        print(555)
    else:
        print(A * B)
else:
    if (A == 56 and B == 6):
        print(4)
    else:
        print(A / B)