import os
os.system("cls")

def factorize(n):
    temp, facs, div = n, "", 2
    while(div <= temp):
        if temp%div==0:
            temp/=div
            facs+=str(div) if facs=="" else " x "+str(div)
        else:
            div+=1

    if facs==str(n):    # if possible change the string application used here!! 
        print("\nThe number",n,"is Prime! Hence its factorization is not possible!\n")
    else:
        print("\nPrime factorization for", n,":\n",n,"= ",facs,"\n", end='')

n = int(input("Enter an integer to prime factorize: "))
factorize(n)
print()

