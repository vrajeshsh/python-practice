import os
os.system("cls")

print("To display positive and negative integers in sepate arrays:")
n = int(input("Enter number of elements: "))

data, pos, neg, i = [], [], [], 0
while i<n:
    print("\nFor Integer #",i+1,": ",sep='')
    type = input("Integer Type ['P' for Positive or 'N' for Negative]: ")
    if type.lower()=="p" or type.lower()=="n":
        num = int(input("Integer: "))
        if type.lower()=="p" and num>0 or type.lower()=="n" and num<0:
            data.append(type)
            data.append(num)
            i+=1
        else:
            print("The Integer does not match its type! Kindly re-enter correctly!\n")
    else:
        print("Invalid type entered! Enter 'P' (for Positive) or 'N' (for negative) only.\n")

print("\nData set as given:\n",data,"\n", sep='')
for i in range(0,n*2-1,2):
    if data[i].lower()=="p":
        pos.append(data[i+1])
    if data[i].lower()=="n":
        neg.append(data[i+1])

print("Positive integers in the data set:\n", pos,
    "\nNegative integers in the data set:\n",neg,sep='')

neg.sort()
pos.sort()

print("\nThe list of intergers and their types:\nINTEGER\t\tTYPE")
for elem in neg+pos:
    print(elem, "\t\t","Negative" if elem<0 else "Positive", sep='')
print()