#Nested For Loop

#part 1
for i in range(1, 11, 1):
    for x in range(1, 11, 1):
        print(x, end=" ")
    print()

#part 2

for i in range(1,11,1):
    for x in range(1, i ,1):
        print(x, end=" ")
    print(i)
