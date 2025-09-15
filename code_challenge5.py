print("Welcome to the Code Challenge 5: THE FACTORIAL PROGRAM")
number = eval(input("Enter any number "))
factorial = 1

for i in range(number, 0, -1):
    factorial *= i
    
print("The Factorial of", number, "is", factorial)
    

