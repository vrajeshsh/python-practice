import os
os.system("cls")

print("To find smallest number which when multiplied by 6 gives a product of only 8's")

num = 0
while True:
    num+= 1
    prod = num*6
    while prod > 0:
        dig = prod%10
        if dig!=8:
            break
        prod//=10
    if prod == 0:
        break

print("\nThe required number is", num, 
    "\nNumber multiplied by 6 yields:", (num*6),"\n")