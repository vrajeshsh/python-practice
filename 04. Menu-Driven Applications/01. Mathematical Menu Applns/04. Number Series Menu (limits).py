import os
os.system("cls")

choice= 0

while choice != 4:
    num = 0
    print("\n\tMISCELLANEOUS NUMBER SERIES",
    "\nOptions available for the series are:",
    "\n1. Series #1: 2, 5, 11, 17, 23...",
    "\n2. Series #2: 1, 2, 5, 13, 34...",
    "\n3. Series #3: 1, 6, 15, 28, 45...",
    "\n4. Exit Program\n")
    choice = int(input("Enter your choice: "))

    if 1<=choice<=3:
        start = int(input("\nEnter the starting limit: "))
        end = int(input("Enter the ending limit: "))
    
    if choice==1:
        sstr, count = "", 0
        for i in range(start, end+1):
            isprime= True
            for j in range(2, i//2+1):
                if i%j==0:
                    isprime= False
                    break
            if i>1 and isprime:
                count+=1
                if count%2 == 1:
                    sstr+= str(i) if sstr=="" else " + "+str(i)
        print("Alternate Prime Series between ",start,"-",end,":\n", 
            sstr, sep='')
     
    elif choice==2:
        sstr, count, a, b = "", 0, -1, 1
        for i in range(start, end+1):
            c = a+b
            a, b = b, c
            count+= 1
            if count%2==0 and start<= c <= end:
                sstr+= str(c) if sstr=="" else " + "+str(c)
        print("Alternate Fibonacci Series between ",start,"-",end,":\n", 
            sstr, sep='')

    elif choice==3:
        sstr, count, num, n = "", 0, 0, 0
        for i in range(start, end+1):
            n+= 1
            num+= n
            count+= 1
            if count%2==1 and start<= num <= end:
                sstr+= str(num) if sstr=="" else " + "+str(num)
        print("Alternate Triangular Number Series between ",start,"-",end,":\n", 
            sstr, sep='')        

    elif choice==4:
        print("\nThe program ends here. Thank You!\n")
    
    else:
        print("\nWrong choice entered! Enter choice betwee 1 - 4 only.\n")
