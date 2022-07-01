import os
os.system("cls")

print("To calculate the result based on numbers and an operator entered:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
opr = input("Enter an operator [+, -, *, /, ^ or % only]: ")

match opr:
    case '+':
        res = num1+num2
    case '-':
        res = num1-num2
    case '*':
        res = num1*num2
    case '/':
        res = round(num1/num2, 2) if num2!=0 else "Infinity"
    case '^':
        res = num1**num2
    case '%':
        res = round(num1/100*num2, 3)   # % is percentage to the non-techy world outside
    case _:
        print("\nInvalid operator entered! Enter operator as [+, -, *, /, ^, %] only.\n")
        exit()

print("\n",num1," ",opr," ",num2," = ",res,"\n", sep='')