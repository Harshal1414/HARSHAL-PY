# h = 36 # Global

# def func1(n):

#     # h = 4
#     global h
#     m = 7
#     h = h + 5
#     # print(n, "I  am done.")
#     print(h, m)
# func1("I am out")

# # print(h, m)



def harry():
    h = 56
    def larry():
        global h
        h = 65
        # print("Before calling larry", h)
        print("After calling larry", h)
    larry()
harry()
