import os
os.system("cls")

choice, neem, dove, liril, lux, payamt= 0, 0, 0, 0, 0, 0

while choice != 5:
    print("\n\tSOAP MENU\n",
        "\n1. Liril Soap [Rs. 25.00 per unit]",
        "\n2. Lux Soap [Rs. 22.50 per unit]",
        "\n3. Dove Soap[Rs. 55.75 per unit]",
        "\n4. Neem Soap [Rs. 35.50 per unit]",
        "\n5. Exit Program")
    choice = int(input("Enter your choice of soap [1-5]: "))
    
    if choice==1:
        qnty = int(input("\nEnter no. of Liril soaps to be bought: "))
        cost = qnty*25
        liril+= qnty
        print("Cost of",qnty,"Liril soaps: Rs",cost)
        
    elif choice==2:
        qnty = int(input("\nEnter number of lux soaps bought: "))
        cost= qnty*22.5
        lux+= qnty
        print("Cost of",qnty,"Lux soaps: Rs",cost)

    elif choice==3:
        qnty = int(input("\nEnter number of dove soaps bought: "))
        cost= qnty*55.75
        dove+= qnty
        print("Cost of",qnty,"Dove soaps: Rs",cost)

    elif choice==4:
        qnty = int(input("\nEnter number of neem soaps bought: "))
        cost= qnty*35.5
        neem+= qnty
        print("Cost of",qnty,"Neem soaps: Rs",cost)

    elif choice==5:
        totalamt = liril*25+lux*22.5+dove*55.75+neem*35.5
        if totalamt>10000:
            payamt= .80*totalamt
        elif totalamt>7500:
            payamt= .85*totalamt
        elif totalamt>5000:
            payamt= .90*totalamt

        print("\nA - Z FANCY DEPARTMENTAL STORE\n\n",
        "# QUANTITY\tUNIT PRICE (Rs)\tAMOUNT (Rs)\n")
        if liril>0:
            print("\n 1. Liril Soap\t",liril,"\t25.00\t",liril*25)
        if lux>0:
            print(" 2. Lux Soap\t",lux,"\t22.50\t",lux*22.5)  
        if dove>0:
            print(" 3. Dove Soap\t",dove,"\t55.75\t",dove*55.75)
        if neem>0:
            print(" 4. Neem Soap\t",neem,"\t35.50\t",neem*35.5)
        print("\n\npayamt Purchase Amount: Rs",totalamt,
        "\nDiscount Enjoyed:",totalamt-payamt,
        "\ntotalamt Payable Amount: Rs",payamt,
        "\n\nThank You! PLEASE VISIT US AGAIN :-)\n")
    
    else:
        print("\nWrong choice entered! Enter choice between 1 - 5 only.\n")
