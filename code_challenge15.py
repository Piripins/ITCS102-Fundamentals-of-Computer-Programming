
#automatic cls for everytime You're running the program
import os
import json

os.system('cls')

print("STUDENT INFORMATION SYSTEM")
print("==========================")


student_record = {}

while True:
    print('A - Add Student Record')
    print('B - Print All Student Record')
    print('C - Search Student Record')
    print('D - Delete Student Record')
    print('E - Edit Student Record')
    print('F - Export Student Record')
    print('G - Import Student Record')
    print('X - Exit Program')

    choice = input("Choose the option you would like to do--> ").lower()

    if choice == 'a':
        #os.system = cls everytime I pick a letter
        os.system('cls')
        print('\nADDING STUDENT RECORD')
        id_no = input("What Is Their Student Number? ")

        surname = input("What Is Their Last Name? ").upper()
        name = input("What Is Their First Name? ").upper()
        age = input("How Old Are They? ")
        section = input("What Section Do They Belong? ").upper()
        course = input("What's Their Course? ").upper()
        student_record[id_no] = [surname, name, age, section, course]
        continue   
    
    elif choice == 'b':
        os.system('cls')
        print('PRINTING STUDENT RECORD')
        for i, j in student_record.items():
            print(f'CODE - {i} INFORMATION {j}')
        continue 
    
    elif choice == 'c':
        os.system('cls')
        print('SEARCHING STUDENT RECORD')
        search = input("What Is Their Student Number? ").lower()
        for id_no in student_record.keys():
            if search in student_record.keys():
                print(f"STUDENT RECORD FOUND for ID {search}")
                
                #printing the searched record
                for i in student_record[search]:
                    print(f" --- {i}")
                    print(" ================= ")
            else:
                print("NO RECORD FOUND")
            break
        continue 
    
    elif choice == 'd':
        os.system('cls')
        print('DELETING STUDENT RECORD')
        search = input("What Is Their Student Number? ").lower()
        for id_no in student_record.keys():
            if search in student_record.keys():
                print(f"STUDENT RECORD FOUND for ID {search}")
                
                for i in student_record[search]:
                    print(f" --- {i}")
                    print(" ================= ")
                student_record.pop(search)
                print("THIS STUDENT RECORD HAS BEEN DELETED")
            else:
                print("NO RECORD FOUND")
            break
        continue 
    
    elif choice == 'e':
        os.system('cls')
        print('EDITING STUDENT RECORD')
        search = input("What Is Their Student Number? ").lower()
        for id_no in student_record.keys():
            if search in student_record.keys():
                print(f"STUDENT RECORD FOUND for ID {search}")
                
                for i in student_record[search]:
                    print(f" --- {i}")
                    print(" ================= ")

                #Palit bagong value 
                surname = input("What Is Their New Last Name? ").upper()
                name = input("What Is Their New First Name? ").upper()
                age = input("What Is Their New Age? ")
                section = input("What NewSection Do They Belong? ").upper()
                course = input("What's Their New Course? ").upper()

                student_record[search][0] = surname
                student_record[search][1] = name        
                student_record[search][2] = age
                student_record[search][3] = section
                student_record[search][4] = course
                
            else:
                print("NO RECORD FOUND")
            break
        continue
    
    elif choice == 'f':
        os.system('cls')
        print("EXPORTING STUDENT RECORD")
        with open('Record_of_student.json', 'w') as new_file:
            json.dump(student_record, new_file, indent=4)
            print("RECORD HAS BEEN EXPORTED")
        continue 

    elif choice == 'g':
        os.system('cls')
        print("IMPORTING STUDENT RECORD")
        with open('Record_of_student.json', 'r') as new_file:
            imported_student = json.load(new_file)

        student_record = imported_student
        print("RECORD HAS BEEN IMPORTED")
        continue 
    
    elif choice == 'x':
        print("You've Exited The Program")
        break
    
    else:
        print("Invalid Input, Re-enter your choice")
        continue
