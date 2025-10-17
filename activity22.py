import random
    
random_number = random.randint(1, 10)
g = True
print("Guess a number") 
tries = 0

while g:
    number = eval(input("Input number here --> "))
    if number != random_number:
        tries +=1
        print("Wrong")
        continue
    elif number == random_number:
        print("You've guess correctly!")
        break
print(f"The number of tries you've made are {tries}")
