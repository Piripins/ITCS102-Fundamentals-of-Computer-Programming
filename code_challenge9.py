print("Welcome to the Code Challenge 9: 🦜 PARROT SIMULATOR – THE ECHO CHAMBER!")

word = input('What would you like your parrot to say ')
number = eval(input("How many times should the parrot squawk it? "))

for i in range(number, 0, -1):
    print("🦜 Squawk!", word)
