# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *
# print("Pattern printing")
# num = int(input("Enter num how many rows you want : "))
# print("Enter 1 or 0")
# bool_val = input("1 for True value or 0 for False : ")
# if bool_val=="1":
#     for i in range(0,num+1):
#         print("*"*i)

# if bool_val=="0":
#     for i in range(num,0,-1):
#         print("*"* i)




print("Patern Printing")

num = int(input("No. of rows you want: "))
print("Enter 1 or 0")
bool_val = input("1 for true value or 0 for false: ")

if bool_val=="1":
    for i in range(0,num+1):
        print("*"*i)

if bool_val=="0":
    for i in range(num,0,-1):
        print("*"*i)