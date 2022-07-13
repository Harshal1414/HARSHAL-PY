# Factorial using Iteration
def iter_factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

# Factorial using Recursion

def rec_factorial(n):
    if n == 1:
        return 1
    else:
        return n * rec_factorial(n-1)

# Fibonacci using recurtion

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter the number: "))
print(fibonacci(number))