'''To find the number with maximum factors'''
print("To find the number with maximum factors:")
n = int(input("Enter number of numbers: "))

print()
for i in range(1,n+1):
    print("Enter number #",i,": ",sep='',end='')
    num = int(input())
    facs,maxi_num,maxi,maxi_facs="",0,0,""
    for j in range(1,num+1):
        count=0
        if num%j==0:
            count+=1
            facs+=str(j) if facs=="" else ", "+str(j)
    if count>maxi:
        maxi=count
        maxi_num = num
        maxi_facs = facs
        
print("\nNumber with most factors:",maxi_num,
    "\nFactors:",facs)
    