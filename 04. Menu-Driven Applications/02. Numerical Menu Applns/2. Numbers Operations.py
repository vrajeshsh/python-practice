import os
os.system("cls")

choice = 0

while choice != 4:
    print("\nTYPE OF NUMBER",
        "\nOptions available are:",
        "\n1. Tech Number",
        "\n2. Pure Number",
        "\n3. Deserium Number",
        "\n4. Exit Program")
    choice = int(input("Enter your choice [1-4]: "))
    if 1<=choice<=3:
        num = int(input("\nEnter an integer: "))
    if choice==1:
        temp, count, ssum = num, 0, 0
        while(temp>0):
            count+=1
            temp//=10

        if count%2==0:
            first = num//(10**(count/2))
            last = num%(10**(count/2))
        ssum = (first+last)**2
        print(num,"is","" if ssum==num else "NOT", "a Tech number.\n")

    elif choice==2:
        temp, count, rev = num, 0, 0
        while(temp>0):
            dig = temp%10
            if dig == 4 or dig==5:
                rev = (rev*10)+dig
                count+=1
                temp//=10
            else:
                break
        print(num,"is","" if (rev==num and count%2 ==0) else "NOT", "a Pure number.\n")

    elif choice==3:
        temp, temp2, ssum, count = num, num, 0, 0
        while(temp>0):
            count+=1
            temp//=10
        while(temp2>0):
            ssum+=(temp2%10)**count
            count-=1
            temp2//=10
        print(num,"is","" if (ssum==num) else "NOT", "a Deserium number.\n")
    elif choice==4:
        print("\nThe program ends here. Thank You!\n")
    
    else:
        print("\nWrong choice entered! Enter choice between 1 - 4 only.\n")
