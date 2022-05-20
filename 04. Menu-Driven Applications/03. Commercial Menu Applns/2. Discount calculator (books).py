import os
os.system("cls")

choice, general, text, help, payamt_gen, payamt_text, payamt_help, payamt = 0, 0, 0, 0, 0, 0, 0, 0

while choice != 4:
    
    print("\n\tBOOK MENU OPTIONS\n",
        "\n1. General Books",
        "\n2. Text Books",
        "\n3. Help Books",
        "\n4. Exit Program")
    choice = int(input("Enter your choice [1-4]: "))
    
    if choice==1:
        buyamt = float(input("\nEnter the purchase amount of General Books: Rs "))
        if buyamt>=2000:
            payamt= .80*buyamt
        general+= buyamt
        payamt_gen+= payamt
        print("Amount to be paid: Rs", buyamt,
        "\nDiscount Enjoyed: Rs",buyamt-payamt,
        "\nAmount to be paid after discount: Rs", payamt)
        
    elif choice==2:
        buyamt = float(input("\nEnter the purchase amount of Text Books: Rs "))
        if buyamt>=5000:
            payamt= .90*buyamt
        text+=buyamt
        payamt_text+=payamt
        print("Amount to be paid: Rs", buyamt,
        "\nDiscount Enjoyed: Rs",buyamt-payamt,
        "\nAmount to be paid after discount: Rs", payamt)

    elif choice==3:
        buyamt = float(input("\nEnter the purchase amount of Help Books: Rs "))
        if buyamt>=2000:
            payamt= .80*buyamt
        help+=buyamt
        payamt_help+=payamt
        print("Amount to be paid: Rs", buyamt,
        "\nDiscount Enjoyed: Rs",buyamt-payamt,
        "\nAmount to be paid after discount: Rs", payamt)
    
    elif choice==4:
        
        print("\nA - Z LIBRARY\n\n",
        "# BOOK TYPE\t\tPURCHASE AMOUNT (Rs)\tDISCOUNT (Rs)\tPAYABLE AMOUNT (Rs)\n")
        if general>0:
            print("\n 1. GENERAL BOOKS\t",general,"\t\t",(general-payamt_gen),"\t",payamt_gen)
        if text>0:
            print(" 2. TEXT BOOKS\t\t",text,"\t\t",(text-payamt_text),"\t",payamt_text)  
        if help>0:
            print(" 3. HELP BOOKS\t\t",help,"\t\t\t",(help-payamt_help),"\t",payamt_help)
        print("\nbuyamtal Purchase Amount: Rs",(general+text+help),
        "\nbuyamtal Discount Enjoyed:",(general+text+help)-(payamt_gen+payamt_text+payamt_help),
        "\nbuyamtal Payable Amount: Rs",(payamt_gen+payamt_text+payamt_help),
        "\n\nThank You! PLEASE VISIT US AGAIN :)\n")
    
    else:
        print("\nWrong choice entered! Enter choice between 1 - 4 only.\n")