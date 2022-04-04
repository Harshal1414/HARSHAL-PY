# FUNCTION and DOCSTRING


# a = 78
# b = 67
# c = sum((a,b))  # built in function.
# print(c)

# user defined function strats from def keyword.

def function1(a,b):
    """This is a function which will calculate SUM of two numbers
    --This function doesnt work for three numbers"""
    print("Hello you are in function 1", a+b)

def function2(a,b):
    """This is a function which will calculate AVERAGE of two numbers
    --This function doesnt work for three numbers"""
    # print("The average is:", (a+b)/2)
    average = (a+b)/2
    # print(average)
    return average

# v = function2(6,7)
# print(v)
print(function2.__doc__)
