import os
os.system("cls")

print("To calculate amount collected from tickets:")

m_amt, f_amt, i = 0, 0, 0

print("\nGo on entering genders [(M)ale/(F)emale] below. Anything else to stop.")
while True:
    i+= 1
    print("Enter gender of Person", i,": ", end='')
    gen = input()
    if gen=='M' or gen=='m':
        m_amt+=50
    elif gen == 'F' or gen=='f':
        f_amt+=35
    else:
        break  
total = m_amt + f_amt

print("\nAmount collected from Males: ", m_amt,
    "\nAmount collected from Females:", f_amt,
    "\nTotal:",total,"\n")
