col = eval(input("Input the amount of columns --> "))

for i in range(1, 11, 1):
    for y in range(1, col+1, 1):
        print(f"{i} X {y} = {y * i}", end="\t")
    print()

for i in range(1, 7, 1):
    for y in range(7, i, -1):
        print(" ",end="")
    for x in range(1, i, 1):
        print("* ",end="")
    print()