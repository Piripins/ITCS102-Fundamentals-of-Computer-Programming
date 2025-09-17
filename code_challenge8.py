print("Welcome to the Code Challenge 8: Multiplication Table Maker")

number = eval(input("Input the number you want to multiply --> "))

if number > 0:
    print('Multiplication table for', number)
    for i in range(1, 11):
        total = number * i
        print(f"{number}X{i} =",total)
else:
    print("Invalid Input")
