# def name_of_students(a, b, c, d):
#     print(a, b, c, d)

# name_of_students("Harshal", "Sukh-E", "Harsh", "Piyush")


def name_args(normal, *names, **bala):    #1.normal argument, 2.args, 3.kwargs
    print(normal)
    for item in names:
        print(item)
    # print(args[2])
    print("\nNow let's introduce some mates and there Duties")
    for key, value in bala.items():
        print(f"{key} is a {value}")


name = "Harshal", "Sukh-E", "Harsh", "Piyush", "Ayush"
statement = "Let's do this!"
Mates = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}

name_args(statement, *name, **Mates)