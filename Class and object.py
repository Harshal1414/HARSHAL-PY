# class myclass:
#     x = 5

# P1 = myclass()
# print(P1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

P1 = Person("john", 53)

print(P1.name)
print(P1.age)