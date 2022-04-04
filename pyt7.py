# Python program if one is eligible to drive or not.

age_group1 = 18

print("Enter your age:")

age_group2 = int(input())

if age_group2>age_group1:
    print("You are eligible to drive")
elif age_group2==age_group1:
    print("No idea what to do")
else:
    print("You are not eligible to drive")