import os
os.system("cls")

def getDiscount(purAmt, choice):
    disc = 0 
    if purAmt <= 1000:
        disc= 0 if choice==1 else 5
    elif purAmt <= 2000:
        disc= 5 if choice==1 else 7.5
    elif purAmt <= 3000:
        disc= 7.5 if choice==1 else 10
    else:
        disc= 10 if choice==1 else 15
    return disc/100*purAmt

choice, tot_amt, tot_disc = 0, 0, 0

print("To calculate payable amount post discount:")
while True:
    print("\nCloth Menu",
            "\nOptions available are:",
            "\n1. Mill Cloth",
            "\n2. Handloom Item",
            "\n3. Exit Program")
    choice = int(input("Enter your choice [1-3]: "))

    if 1<=choice<=2:
        purAmt = float(input("Enter the Purchase Amount: Rs "))
        discount = getDiscount(purAmt, choice)
        tot_amt+=purAmt
        tot_disc+=discount
        print("\nDiscount: Rs", discount,
            "\nPayable Amount: Rs",purAmt-discount)
    
    elif choice==3:
        print("\nTotal Purchase Amount: Rs", tot_amt)
        print("Total Discount enjoyed: Rs", tot_disc)
        print("\nThankyou for shopping. Do visit again :)\n")
        break
    
    else:
        print("\nKindly select an option between 1 and 3.\n")
    