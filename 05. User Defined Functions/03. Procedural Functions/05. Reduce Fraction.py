import os
os.system("cls")

# def showFraction(num, den):
#     i, frac, sign = 2, "", ""
#     if (num>0 and den<0) or (num<0 and den>0):
#         sign = "-"
#     num, den = abs(num), abs(den)
#     while i<min(num,den)+1:
#         if num%i==0 and den%i==0:
#             num//=i
#             den//=i
#             frac = sign+str(num)+("/"+str(den) if den!=1 else "")
#         else:
#             i+=1
#     print("\nThe reduced fraction:",frac,"\n")

def showFraction(num, den):
    for i in range(1, min(abs(num), abs(den))+1):
        if num<0 and den<0:
            num = abs(num)
            den = abs(den)
        if num%i==0 and den%i==0:
            hcf = i
    num//=hcf
    den//=hcf
    print("\nThe reduced fraction: ",num,"/",den,"\n", sep='')

num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))

showFraction(num, den) if den!=0 else print("\nDivision by 0 error!\n")