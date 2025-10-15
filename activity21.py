baho_si_Go = True

while baho_si_Go:
    confirm = input("Does Francis needs to continue showering? (yes/ no) ").lower()
    if confirm == 'yes':
        print("*Francis' continues to shower/*")
        continue
    else:
        print("Francis smells too much for showers to work", ", YUCK BAHO!")
        break
