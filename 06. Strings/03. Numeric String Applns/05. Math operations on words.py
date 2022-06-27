import os
os.system("cls")

def calculate(num1, num2, opr): 
    result= 0
    if opr=="+":
        result= num1+num2 
    elif opr=='-':
        result= num1-num2 
    elif opr=='*':
        result= num1*num2 
    elif opr=='/':
        result= num1/num2 
    return result

result, word, count = 0, "", 0

print("To perform mathematical operations on embeded integers in a sentence:")
sent = input("Enter the sentence:\n").strip()+" "
opr = input("Enter operation symbol [+,-,*,/]: ")

for ch in sent:
    if ch.isalnum():
        word+=ch
    elif word!="":
        if word.isdigit():
            num = int(word)
            count+=1
            result= num if count==1 else calculate(result, num, opr)
        word=""

print("\nResult:", result,"\n")