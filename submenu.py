import os 
import time

def menu():
        print('''\t------------------------------
                    \n\t\t"MAIN MENU"                        

            1. Print Statements
            2. Variable
            3. Operators
            4. Conditional Statements
            5. Loops
            6. List
            7. Functions
            8. Run Your Own Code
            0. Exit                       
                                   
        ------------------------------                       
                                            ''')





#This is for printing statements
def printmenu():
    while True: 
        print('\n1. Basic Printing')
        print('2. Print With Concatenation')
        print('3. Definition')
        print('0. Back To Main Menu')

        option = input('Enter The Option You Want To Proceed With--> ')
        
        #Option 1 is for the output and inputs of print statements
        if option == '1':
             os.system('cls')
             print('\n======================================')
             print('\nINPUT: \nprint("Hello, World") \nprint("Welcome To The Matrix") \nprint("You Are The Best")')
             print('\n======================================')
             print('\nOUTPUT: \nHello World \nWelcome To The Matrix \nYou Are The Best')
             continue
        
        #Option 2 is the same but with concatenations
        elif option == '2':
            os.system('cls')
            print('\n======================================')
            statement1 = input('Enter Your First Input--> ')
            statement2 = input('Enter Your Second Input--> ')
            result = statement1 + ' ' + statement2
            print(result)
            print('\n======================================')

            bano = input('Do You Want To See How It Worked? (Y/N) ').lower()

            if bano == 'y': 
                print('\n======================================')
                print('\nInput: \nstatement1 = input("Enter Your First Input--> ") \nstatement2 = input("Enter Your Second Input--> ") \nresult = statement1 + " " + statement2 \nprint(result)')
                print(f'\nOutput: {result}')
                print('\n======================================')
                continue
            
            elif bano == 'n':
                print('Returning....')
                time.sleep(0.5)
                continue
            else:
                print('Invalid Input Please Try Again')
                continue
                
        
        #option 3 is for definition
        elif option == '3':
            os.system('cls')
            print('\n======================================')
            print('''Printing in programming is primarily used to display 
information to the user or for debugging purposes. It 
allows developers to see the output of their code, which 
can include text, variables, or other data types. This is 
essential for understanding how a program is functioning
and for troubleshooting issues.''')
            print('\n======================================')
        #Option 0 is for going back to the menu
        elif option == '0':
            print('Returning To Main Menu.....')
            time.sleep(1)
            break
        
        else: 
            print('Invalid Option Please Try Again')



#for variables
def variablesmenu():
    while True:
        print('\n1. Plus And Concatenation \nOf Printing With Variables \n(Try An Example)')
        print('2. Explanation')
        print('3. Definition')
        print('0. Back To Main Menu')

        option = input('Enter The Option You Want To Proceed With--> ')
        
        #Option 1 
        if option == '1':
            
            pick = input('1. STATEMENTS 2. NUMBERS (addition)? (Pick 1 or 2)--> ')
            
            if pick == '1':
                print('\n======================================')
                statement1 = input('Enter Your First Input--> ')
                statement2 = input('Enter Your Second Input--> ')
                result = statement1 + ' ' + statement2
                print('\nOUTPUT:')
                print(result)
                print('\n======================================')

    
            elif pick == '2':
                print('\n======================================')
                print('Enter The Numbers You Want To Add')
                num1 = int(input('Enter The First Number--> '))
                num2 = int(input('Enter The Second/Last Number--> '))
                sum = num1 + num2 
                print('\nOUTPUT:')
                print(sum)
                print('\n======================================')
               

            else:
                print("Invalid Input Please Try Again")
                continue
        
        #Option 2 
        elif option == '2':
            os.system('cls')
            print('\n======================================')
            print('\n EXPLANATION FOR STATEMENTS')
            print('\nInput: \nstatement1 = input("Enter Your First Input--> ") \nstatement2 = input("Enter Your Second Input--> ") \nresult = statement1 + " " + statement2 \nprint(result)')
            print(f'\nOutput: {result}')
            print('\nThe Variables Used Here Are "statement1" And "statement2"')
            print('\n======================================')
            
            print('\n======================================')
            print('\nEXPLANATION FOR NUMBERS')
            print('\nINPUT: \nnum1 = int(input("Enter The First Number")) \nnum2 = int(input("Enter The Second/Last Number")) \nsum = num1 + num2 \nprint(sum)')
            print(f'\nOUTPUT: {sum} ')
            print('\nThe Variables Used Here Are "num1" And "num2"')
            print('\n======================================')
            
    
        #option 3 is for definition
        elif option == '3':
            os.system('cls')
            print('\n======================================')
            print('''Variables are symbolic names that reference objects. 
They are created by assigning a value to a name using the equals sign (=).''')
            print('\n======================================')
        #Option 0 is for going back to the menu
        elif option == '0':
            print('Returning To Main Menu.....')
            time.sleep(1)
            break
        
        else: 
            print('Invalid Option Please Try Again')



#FOR OPERATORS
def operatorsmenu():
    while True:
        print('1. Operators (Try An Example)')
        print('2. Explanation')
        print('3. Definition')
        print('0. Back To Main Menu')
     
        option = input('Enter The Option You Want To Proceed With--> ')
        
        #Option 1 
        if option == '1':
            print('\n======================================')
            a = eval(input('Input Your FIrst Number--> '))
            b = eval(input('Input Your Second Number--> '))
            
            print('ADDITION')
            print(a + b) 
            
            print('SUBTRACTION')
            print(a - b) 
        
            print('MULTIPLICATION')
            print(a * b) 
            
            print('DIVISION')
            print(a / b) 
            
            print('MODULUS')
            print(a % b) 
            
            print('EXPONENTIATION')
            print(a ** b) 
            
            print('FLOOR DIVISION')
            print(a // b) 
           
            print('\n======================================')
       

        #Option 2 
        elif option == '2':
            print('\n======================================')
            print('''a = eval(input('Input Your FIrst Number--> ')) \nb = eval(input('Input Your Second Number--> '))
            print(a + b) 
            print(a - b) 
            print(a * b) 
            print(a / b) 
            print(a % b) 
            print(a ** b) 
            print(a // b)''')
            print('\n======================================')
    
        #option 3 is for definition
        elif option == '3':
            os.system('cls')
            print('\n======================================')
            print('''Operators are special symbols that perform operations on variables and values. \nThey are essential for performing arithmetic, logical, comparison, and other operations. ''')
            print('\n======================================')
        
        #Option 0 is for going back to the menu
        elif option == '0':
            print('Returning To Main Menu.....')
            time.sleep(1)
            break
        
        else: 
            print('Invalid Option Please Try Again')



#FOR CONDITIONAL STATEMENTS
def conditionalmenu():
    while True:
        print('1. Conditional Statement (Try An Example)')
        print('2. Explanation')
        print('3. Definition')
        print('0. Back To Main Menu')
     
        option = input('Enter The Option You Want To Proceed With--> ')
        
        #Option 1 
        if option == '1':
            print('\n======================================')
            score = int(input("Enter your score: "))
            if score >= 90:
                print("Grade: A")
            elif score >= 75:
                print("Grade: B")
            elif score >= 65:
                print("Grade: C")
            else:
                print("Grade: F")
            print('\n======================================')
            continue
       
        #Option 2 
        elif option == '2':
            print('\n======================================')
            print('''score = int(input("Enter your score: "))
        if score >= 90:
            print("Grade: A")
        elif score >= 75:
            print("Grade: B")
        elif score >= 65:
            print("Grade: C")
        else:
            print("Grade: F")''')
        
            print('\n======================================')
            continue
    
        #option 3 is for definition
        elif option == '3':
            os.system('cls')
            print('\n======================================')
            print('''Conditional statements are used to make decisions in your program — 
they allow you to execute certain blocks of code only if specific conditions are met. 
This use if, elif, and else for creating conditions for each variables and statements. ''')
            print('\n======================================')
            continue
        
        #Option 0 is for going back to the menu
        elif option == '0':
            print('Returning To Main Menu.....')
            time.sleep(1)
            break
        
        else: 
            print('Invalid Option Please Try Again')


#FOR LOOPS
def loopmenu():
    while True:
        print('1. For Loops')
        print('2. While Loops')
        print('3. Nested For Loops')
        print('4. Explanation')
        print('5. Definition')
        print('0. Back To Main Menu')
     
        option = input('Enter The Option You Want To Proceed With--> ')
        
        #Option 1 
        if option == '1':
            print('\n======================================')
            
            for i in range(5):
                print(i)

            print('\n======================================')
            continue
       
        #option 2
        if option == '2':
            print('\n======================================')
            i = 1
            while i <= 3:
                print(i)
                i += 1
            else:
                print("Loop ended")            
            
            print('\n======================================')
            continue
        
        #option 3
        if option == '3':
            print('\n======================================')
            for i in range(11, 1, -1):
                for x in range(1, i, 1):
                    print("*", end=" ")
                print()   
            print('\n======================================')
            continue

        #Option 4 
        elif option == '4':
            print('\n======================================')
            print('NORNAL FOR LOOP')
            
            print('''            for i in range(5):
                print(i) ''')
            
            print('WHILE LOOP')
            
            print('''            i = 1
            while i <= 3:
                print(i)
                i += 1
            else:
                print("Loop ended")      ''')

            print('NESTED FOR LOOP')
            
            print('''            for i in range(11, 1, -1):
                for x in range(1, i, 1):
                    print("*", end=" ")
                print()   ''')
            print('\n======================================')
            continue
    
        #option 5 is for definition
        elif option == '5':
            os.system('cls')
            print('\n======================================')
            print('''Loops in Python are constructs used to execute a block of code repeatedly, 
either for a fixed number of iterations or until a specific condition is met. 
They are essential for automating repetitive tasks and improving code efficiency.''')
            print('\n======================================')
            continue
        
        #Option 0 is for going back to the menu
        elif option == '0':
            print('Returning To Main Menu.....')
            time.sleep(1)
            break
        
        else: 
            print('Invalid Option Please Try Again')


#FOR LISTS
def listmenu():
    while True:
        print('1. List')
        print('3. Definition')
        print('0. Back To Main Menu')
     
        option = input('Enter The Option You Want To Proceed With--> ')    

        #option 1
        if option == '1':
            print('\n==============================')
            
            print('\nNORMAL LIST')
            print('''\nInput: 
                fruit = ['Dalanghita', 'Ubas', 'Mansanas']  
                print(fruit)
                
                Output: 
                ['Dalanghita', 'Ubas', 'Mansanas']''')
            
            print('\nWith Append')
            print('''\nInput: 
                fruit = ['Dalanghita', 'Ubas', 'Mansanas'] 
                print(fruit)
                
                fruit.apppend('Orange')
                  
                Output: 
                ['Dalanghita', 'Ubas', 'Mansanas', 'Orange']''')
            
            print('\nWITH POP')  
            print('''\nInput: 
                fruit = ['Dalanghita', 'Ubas', 'Mansanas']  
                print(fruit)
                
                fruit.pop()
                  
                Output: 
                ['Dalanghita', 'Ubas']''')

            print('\nWITH INSERT')
            print('''\nInput: 
                fruit = ['Dalanghita', 'Ubas', 'Mansanas']  
                print(fruit)
                
                fruit.inser(1, 'Lansones')
                  
                Output: 
                ['Dalanghita', 'Lansones', 'Ubas', 'Mansanas']''')
            
            print('\nWITH REMOVE')
            print('''\nInput: 
                fruit = ['Dalanghita', 'Ubas', 'Mansanas']  
                print(fruit)
                  
                fruit.remove('Dalanghita')
                
                Output: 
                ['Ubas', 'Mansanas']''')
            
            print('\nWITH SORT')
            print('''\nInput: 
                fruit = ['Dalanghita', 'Ubas', 'Mansanas']  
                print(fruit)
                
                fruit.sort()
                  
                Output: 
                ['Dalanghita','Mansanas', 'Ubas']''')
            
            print('\nWITH REVERSE')
            print('''\nInput: 
                fruit = ['Dalanghita', 'Ubas', 'Mansanas']  
                print(fruit)
                
                fruit.reverse()

                Output: 
                ['Mansanan', 'Ubas', 'Mansanas']''')
            print('\n==============================')
            
            
        #option 2 is for definition
        elif option == '2':
            os.system('cls')
            print('\n======================================')
            print('''Lists are versatile and powerful data structures that allow you to store and manipulate 
                  collections of items. Lists are ordered, changeable, and allow duplicate values.  ''')
            print('\n======================================')
            continue
        
        #Option 0 is for going back to the menu
        elif option == '0':
            print('Returning To Main Menu.....')
            time.sleep(1)
            break

#FOR FUNCTIONS
def functionmenu():
    while True:
        print('1. Functions')
        print('3. Definition')
        print('0. Back To Main Menu')
     
        option = input('Enter The Option You Want To Proceed With--> ')    

        #option 1
        if option == '1':
            print('\n==============================')
            print('''INPUT:
            def sum(a, b):
                return (a + b)

            a = int(input('Enter 1st number: '))
            b = int(input('Enter 2nd number: '))

            print(f'Sum of {a} and {b} is {sum(a, b)}')''')
            print('''OUTPUT:
                  Enter 1st number: __
                  Enter 2nd number: __
                  Sum of __ and __ is __''')
            print('\n==============================')
       
        #option 2 is for definition
        elif option == '2':
            os.system('cls')
            print('\n======================================')
            print('''A function is a block of code that performs a specific task and can be reused multiple times. 
Functions help in organizing code, making it more readable, and reducing redundancy. ''')
            print('\n======================================')
            continue
        
        #Option 0 is for going back to the menu
        elif option == '0':
            print('Returning To Main Menu.....')
            time.sleep(1)
            break

#FOR TRYING IT YOURSELF
def sarilimenu():
    print('\n======================================')
    print('''\nCongratulations On Learning How To Code! In This Section, 
You Can Create Your Own Code, And Execute It. 
Below Are The Options On What Type Of Code You Would Like To Perform 

Good Luck On Your Coding Journey!!''')
    print('\n======================================')
    while True:
        print('''
            1. Print Statements
            2. Variable
            3. Operators
            4. Conditional Statements
            5. Loops
            6. List
            7. Functions
            0. Back To Main Menu''')
        
        option = input('\nEnter The Option You Want To Proceed With--> ')  

        if option == '1':
            printing = input('\nCreate Your Own Print Statement: ')
            exec(printing)
            time.sleep(1)
            continue

        elif option == '2':
            variables = input('\nCreate Your Own Varaibles Statement: ')
            exec(variables)
            time.sleep(1)
            continue      

        elif option == '3':
            operators = input('\nCreate Your Own Operators Statement: ')
            exec(operators)
            time.sleep(1)
            continue

        elif option == '4':
            condtional_statements = input('\nCreate Your Own Conditional Statement: ')
            exec(condtional_statements)
            time.sleep(1)
            continue

        elif option == '5':
            loops = input('\nreate Your Own Loops: ')
            exec(loops)
            time.sleep(1)
            continue

        elif option == '6':
            listing = input('\nCreate Your Own Lists: ')
            exec(listing)
            time.sleep(1)
            continue

        elif option == '7':
            functions = input('\nCreate Your Own Functions: ')
            exec(functions)
            time.sleep(1)
            continue

        elif option == '0':
            print('Returning To Main Menu....')
            time.sleep(0.5)
            break
        else:
            print('Invalid Input Please Try Again')
        
        print('\n======================================') 