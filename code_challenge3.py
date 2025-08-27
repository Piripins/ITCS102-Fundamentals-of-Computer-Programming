name = input("What is your name? -> ")
fare = eval(input("Please insert your fee -> "))
isStudent = input("Are you a Student? -> ")

if isStudent.lower() == 'yes': 
	print("Your amount will be discounted by 20 percent")
	discount = fare * 0.2
	new_fare = fare - discount 
	sukli = fare - new_fare
	print("Your fee", fare,  "has been discounted")
	print("You have paid", new_fare)
	print("Your change is", sukli)

else:
	print("Sorry", name , "You will not be discounted by 20 percent")
	print("You have paid", fare ,)





	
