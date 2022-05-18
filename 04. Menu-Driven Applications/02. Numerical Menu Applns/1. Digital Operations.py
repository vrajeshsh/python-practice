import os
os.system("cls")

choice = 0

while choice != 4:
    print("\nDIGITAL OPERATIONS",
        "\nOptions available are:",
        "\n1. Digital Mean",
        "\n2. Digital Double",
        "\n3. Digital root",
        "\n4. Exit Program")
    choice = int(input("Enter your choice [1-4]: "))

    if 1<=choice<=3:
        num = int(input("\nEnter an integer: "))
    if choice==1:
        temp, count, ssum = num, 0, 0
        while(temp>0):
            count+=1
            ssum+= temp%10
            temp//=10
        avg = ssum/count
        print("Digital Mean of", num,":",round(avg,3),"\n")

    elif choice==2:
        temp, count = num, 0
        while(temp>0):
            dig = temp%10
            count+=1
            temp//=10
        dig_double = num*(10**count)+num
        print("Digital Double of", num,":",dig_double,"\n")

    elif choice==3:
        temp, ssum = num, 0
        while(temp>0 or ssum>9):
            if temp==0:
                temp = ssum
                ssum = 0
            ssum+=temp%10
            temp//=10
        print("Digital Root of", num,":",ssum,"\n")
    
    elif choice==4:
        print("\nThe program ends here. Thank You!\n")
    
    else:
        print("\nWrong choice entered! Enter choice betwee 1 - 4 only.\n")
