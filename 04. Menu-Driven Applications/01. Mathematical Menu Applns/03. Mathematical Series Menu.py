import os
os.system("cls")

choice= 0

while choice != 4:

    print("\nMATHEMATICAL SERIES MENU",
    "\nOptions available are:",
    "\n1. 5 + 55 + 555 + n...",
    "\n2. 1/3 + 8/5 + 27/7 + n",
    "\n3. 1 + 2/2! + 3/3! + 5/5! + n...",
    "\n4. Exit Program\n")
    choice = int(input("Enter your choice (1 - 4): "))
    
    if 1<=choice<=3:
        n = int(input("Enter the no. of terms(n) for the series: "))
    if choice==1:
        ssum, num = 0, 0 #
        for i in range(n):
            num+= 5*(10**i)
            print(num if i==0 else " + "+str(num), end='')
            ssum+=num
        
    elif choice==2:
        ssum= 0
        for i in range(1, n+1):
            num= i**3/(2*i+1)
            print(num if i==1 else " + "+str(num), end='')
            ssum+=num

    elif choice==3:
        ssum= 0
        for i in range(1, n+1):
            fact=1
            for j in range(1, i+1):
                fact*= j
            num=i/fact
            print(num if i==1 else " + "+str(num), end='')
            ssum+=num
    
    elif choice==4:
        print("\nThe program ends here. Thank You!\n")
    
    else:
        print("\nWrong choice entered! Enter choice betwee 1 - 4 only.\n")
    
    if 1<=choice<=3:    
        print("\nSum of the series: ", ssum)
    