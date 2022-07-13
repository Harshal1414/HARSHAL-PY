# F string

import math

m ="Harshal Patel"

# a = "This is %s"%m
# print(a)
d = "from BAHERI"

# a = "This is {1} {0}"  #Using indexes 
# b = a.format(m, d)   # String formatting
# print(b)


a = f"This is {m} {d} {math.cos(78)}"  # F-String
print(a)