print("Welcome to the Code Challenge 7: Project Liftoff")

confirmation = input("Would like to start Project Liftoff (Yes/No) ")

if confirmation == "yes":  
    print("Countdown is starting")
    for i in range(5, 0, -1):
        print(f"{i}")
    print("Liftoff!")
else:
    print("Okay, see you next time trooper!")
