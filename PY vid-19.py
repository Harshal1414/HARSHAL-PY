# i=0
# while(True):
#     i=i+1
#     if(i==5):
#         continue
#     if(i>10):
#         break
#     print(f"The value of i is : {i}")


# QUIZ

# while(True):
#     i = int(input("Enter a number:\n"))
#     if i>100:
#         print("congrats! You have Entered a number greater than 100\n")
#         break
#     else:
#         print("Please, Try again\n")
#         continue

i = 0
while (True):
    if i+1<5:
        i=i+1
        continue
    print(i+1, end=" ")
    if (i==45):
        break
    i = i+1