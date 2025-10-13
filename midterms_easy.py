for i in range(1, 6, 1):
    for x in range(6, i, -1):
        print(" ", end="")
    for y in range(1, i*2, 1):
        print("*", end="")
    print()

for i in range(1, 6, 1):
    for y in range(1, i+1, 1):
        print(i, end="")
    print()