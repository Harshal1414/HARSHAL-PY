numbers = ["3", "56", "34"]
numbers = list(map(int, numbers))
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

numbers[1] = numbers[1] + 4
# print(numbers[1])

# def sq(a):
#     return a*a
# num = [2,4,332,44,56]
# square = list(map(sq, num))
# print(square)

num = [2,4,332,44,56]
square = list(map(lambda x:x*x, num))
print(square)