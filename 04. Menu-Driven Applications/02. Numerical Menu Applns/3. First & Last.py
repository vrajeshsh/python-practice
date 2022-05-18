import os
os.system("cls")

choice = 0

while choice != 4:
    print("\nNUMBER GENERATOR",
        "\nOptions available are:",
        "\n1. Middle digits equal to Sum of First & Last",
        "\n2. Sum of middle digits equal to Product of First & Last",
        "\n3. Each of middle digits is factor of Product of First & Last",
        "\n4. Exit Program")
    choice = int(input("Enter your choice [1-4]: "))
    if choice==1:
        cnt= 0
        #nos = ""
        for i in range(100, 10000):
            count, last, temp = 0, i%10, i
            while temp>0:
                first = temp%10
                count+=1
                temp//=10
            mid = (i//10)%(10**(count-2))
            if (first+last)==mid:
                cnt+= 1
                print(i if cnt==1 else ", "+str(i), end= '')
                #nos+= str(i) if nos=="" else ", "+str(i)
        print("\n")

    elif choice==2:
        for i in range(100, 10000):
            count, ssum = 0, 0
            last = i%10
            temp = i
            while temp>0:
                first = temp%10
                count+=1
                temp//=10
            mid = (i//10)%(10**(count-2))
            
            while(mid>0):
                ssum+=mid%10
                mid//=10
            if (first*last)==ssum:
                print(",",i, end='') 

        print("")
    elif choice==3:
        
        for i in range(100, 10000):
            count, isFactor = 0, True
            last = i%10
            temp = i
            while temp>0:
                first = temp%10
                count+=1
                temp//=10
            mid = (i//10)%(10**(count-2))
            if mid>1:
                while(mid>0):
                    dig = mid%10
                    if dig==0 or last==0 or (first*last)%dig!=0:
                        isFactor=False
                        break
                    mid//=10
                if isFactor:
                    print(",",i, end='')
        print("")
    elif choice==4:
        print("\nThe program ends here. Thank You!\n")
    
    else:
        print("\nWrong choice entered! Enter choice betwee 1 - 4 only.\n")
