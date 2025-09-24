number = 100

print("Input Ten (10) numbers to subtract to the number 100")

for i in range(1, 11, 1):
    x = eval(input(f"{i} - Input the number here --> "))
    number -= x
print(f"This is the total ({number})")