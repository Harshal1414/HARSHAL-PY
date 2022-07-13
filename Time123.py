import time

initial = time.time()
print(initial)

k = 0
while (k<7):
    k+=1
    time.sleep(1)
    print("Harshal is a good boy.")
print("while loop ran in", time.time() - initial, "Seconds\n")

initial2 = time.time()

for i in range(8):
    print("Harshal is a CODER.")
print("for loop ran in", time.time() - initial, "Seconds\n")

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)