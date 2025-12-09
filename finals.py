from test import *
import os 
import time, sys 

os.system('cls')


print('\nWelcome to LEARNING PYTHON')
print('==========================')

pangalan = input('What Is Your Name? ').upper()

agreement = input(f'\nHello {pangalan}, Are You Ready To Learn Python? (Y/N) ').lower()

if agreement == 'y':
    for i in range(21):
        bar = "█" * i + '-' * (20-i)
        sys.stdout.write(f'\rLoading: [{bar}] {i*5}%')
        sys.stdout.flush()
        time.sleep(0.2)
    os.system('cls')

while True: 
    if agreement == 'y':
        menu()
        choice = input('Enter The Number Of Your Chosen Topic--> ')
            
        if choice == '1':
            printmenu()
            continue
        elif choice == '2':
            variablesmenu()
            continue
        elif choice == '3':
            operatorsmenu()
            continue
        elif choice == '4':
            conditionalmenu()
            continue
        elif choice == '5':
            loopmenu()
            continue
        elif choice == '6':
            listmenu()
            continue
        elif choice == '7':
            functionmenu()
            continue
        elif choice == '8':
            sarilimenu()
            continue
        elif choice == '0': 
            time.sleep(0.5)
            print('\nThank You For Using This Program!')
            time.sleep(0.5)
            print('I Hope You Learned Something!')
            time.sleep(0.5)
            print('Exiting Program....')
            time.sleep(0.5)
            break
        else:
            print('Invalid Option Please Try Again')
            continue
    
    elif agreement == 'n':
        print(f'Thank You For Opening The Program, {pangalan}')
        break
        
    
    else: 
        print('Invalid Input Please Try Again')