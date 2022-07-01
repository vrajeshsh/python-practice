import os
os.system("cls")

print("To display the day corresponding to a day number entered:")
daynum = int(input("Enter the day number [1 - 7]: "))

match daynum:
    case 1: 
        day = "Sunday"
    case 2: 
        day = "Monday"
    case 3: 
        day = "Tuesday"
    case 4: 
        day = "Wednesday"
    case 5: 
        day = "Thursday"
    case 6: 
        day = "Friday"
    case 7: 
        day = "Saturday"
    case _:
        print("\nInvalid day number entered! Enter day number between 1 - 7 only.\n")
        exit()

print("\nThe day number '", daynum, "' represents the ", day,".\n", sep='')    
