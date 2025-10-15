print("Welcome to my Code Challenge 13")

name = input("What is your name? ")
sum = 1
sama_sama = " " 
g = True

print("+++++++++++++++++++++++++++++++ \n\tType 0 to stop \n+++++++++++++++++++++++++++++++")


while g:
    num = eval(input("Input a random number --> "))
    
    if num %2 == 1:
        print("This number is an ODD number")
        sum += num
        sama_sama += str(num) + " "
    elif num == 0:
        print("TIGIL!!!")
        break
    else:
        if num %2 == 0:
            print("This number is an EVEN number")
        else:
            print(f"Oh no, {num} it's not a number")
print(f"Hi {name}!, the sum of all ODD number is {sum}")    
print(f"The odd numbers are {sama_sama}")
        
    
    