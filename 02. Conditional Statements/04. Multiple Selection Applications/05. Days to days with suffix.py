import os
os.system("cls")

print("To display date entered with suffix: ")
temp = num = int(input("Enter the number [1 - 31]: "))

temp = num if num==11 or num==12 or num==13 else num%10 
if num<32:
    match temp:
        case 1:
            suffix = "st"
        case 2:
            suffix = "nd"
        case 3:
            suffix = "rd"
        case 4 | 5 | 6 | 7 | 8 | 9 | 0 | 11 | 11 | 12 | 13:
            suffix = "th" 
else:
    print("\nInvalid day number entered! Enter day number between 1 - 31 only.\n")
    exit()

print("\nAfter adding suffix: ",num,suffix,"\n", sep='')    