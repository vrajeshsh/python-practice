import os
os.system("cls")

print("To display the number of days in a month:")
month = input("Enter the month (January - December): ").title()

match month:    
    case "January" | "March" | "May" | "July" | "August" | "October" | "December":    
        days = 31
    case "April" | "June" | "September" | "November":
        days = 30
    case "February":
        days = 28
    case _:
        print("\nInvalid month entered! Enter month between January - December only.\n")
        exit()

print("\nThe month number '", month, "' has ", days," days.\n", sep='') 
