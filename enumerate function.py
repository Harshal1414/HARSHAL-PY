list = ["bhindi", "Gobhi", "aaloo", "Paneer"]

# Without using ENUMERATE

# i = 1
# for item in list:
#     if i%2 == 0:
#         print(item)
#     i += 1

# Using ENUMERATE

for index, item in enumerate(list):
    if index%2 != 0:
        print(f"Please buy {item}")