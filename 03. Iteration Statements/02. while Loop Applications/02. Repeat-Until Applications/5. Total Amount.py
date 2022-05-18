import os
os.system("cls")

print("To calculate amount collected from tickets:")

i, count1,count2,count3,count4 = 0, 0, 0, 0, 0

while True:
    i+= 1
    print("Enter age for Person", i,": ", end='')
    age = int(input())
    if age<=0:
        break
    if age>59:
        count1+=1
    elif age>19:
        count2+=1
    elif age>4:
        count3+=1
    elif age>0:
        count4+=1
total = count2*30+count3*40

print("\nCATEGORY\tNO. OF PEOPLE\n",
    "\nBelow 4\t\t",count4,"\n4 - 18\t\t",count3,
    "\n19 - 59\t\t",count2,"\nAbove 59\t",count1,
    "\n\nTotal amount: Rs",total,"\n",sep='')