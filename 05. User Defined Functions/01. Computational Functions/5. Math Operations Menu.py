import os
os.system("cls")

def getResult(num1, num2, opr):
    res = 0
    if opr=="+":
        res = num1+num2
    elif opr=="-":
        res = num1-num2
    elif opr=="*":
        res = num1*num2
    elif opr=="/":
        if num2!=0:
            res = num1/num2
        else:
            res= "Infinity" 
    elif opr=="^":
        res = num1**num2
    elif opr=="%":  # % is percentage in the real worl
        res = num1/100*num2
    else:
        res= "Wrong operator used!\n"
    return res

print("To perform simple arithmetic with numbers:")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
opr = input("Enter the operator [+, -, *, /, ^, %]: ")

res= getResult(num1, num2, opr) 
if res == "Wrong operator used!\n":
    print(res)
else:
    print("\n",num1," ",opr," ",num2," = ", res, "\n",sep="")    
