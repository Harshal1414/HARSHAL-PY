list1 = [ ["Harry", 1], ["Larry", 2],
          ["Carry", 6], ["Marie", 250]]
dict1 = dict(list1)

for item in dict1:
    print(item)
for item, lollypop in dict1.items():
    print(item, "and lolly is ", lollypop)
