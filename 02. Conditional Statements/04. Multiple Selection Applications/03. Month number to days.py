from ast import Or
import os
os.system("cls")

print("To display no. of days in month corresponding to month number:")
month_num = int(input("Enter month number [1 - 12]: "))

match month_num:    # In 2022, if you think match-case in Python should be done 'this way' then...
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        days = 31
    case 4 | 6 | 9 | 11:
        days = 30
    case 2:
        days = 28
    case _:
        print("\nInvalid month number entered! Enter month number between 1 - 12 only.\n")
        exit()

print("\nThe month number '", month_num, "' has ", days," days.\n", sep='') 

# '|' is a bitwise operator of Python... it's a boolean operator working in lieu of or
# || and | are not the same 
# || is the boolean operator Or
# | is the bitwise operator (version) for the boolean operator ||
