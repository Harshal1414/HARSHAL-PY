#  Lambda is a one liner function - Anonymous function.

def add(a,b):
    return a+b

minus = lambda a,b : a-b  # Lambda function

a = int(input("a = "))
b = int(input("b = "))
print("The difference is", minus(a,b))