import os
os.system("cls")

print("To display the type of an entered character:")
char = input("Enter the character: ")

if char.isalpha():
    type = "Alphabet"
elif char.isdigit():
    type = "Digit"
else:
    match char:
        case ' ':
            type = "Space"
        case '?' | '.' |'!' |',' |';' | ':'|'-'|'"'|'\'':
            type = "Punctuation"
        case '\n' | '\t':
            type = "Control Charcter"
        case _:
            type = "Symbol"

print("\nThe type of '", char,"' is: ", type,"\n", sep='')
