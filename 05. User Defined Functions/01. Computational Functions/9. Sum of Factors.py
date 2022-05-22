import os
os.system("cls")

def sumOfFactors(num):
    ssum = 0
    for i in range(1, num//2+1):
        if num%i==0:
            ssum+=i
    return ssum

print("To check if number is Perfect, Prime or Unclassified:")
n = int(input("Enter the number of integers: "))
for i in range(1, n+1):
    status = ""
    print("Enter number #",i,": ", end='')
    num = int(input())
    if num<2:
        status = "Unclassified"
    else:
        facsum = sumOfFactors(num)      # you will never learn!!
        if facsum == num: 
            status = "Perfect"
        else:
            status = "Imperfect"
        if facsum==1:
            status+=" and Prime"
        else:
            status+=" and Composite"
    
    print("\nThe integer",num,"is:",status,"\n")
    
    
