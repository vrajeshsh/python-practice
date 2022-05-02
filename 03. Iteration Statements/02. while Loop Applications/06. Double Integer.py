print("To double an integer digitally:")
num = int(input("Enter an integer: "))

temp,count=num,0
while(temp>0):
    dig=temp%10
    count+=1
    temp//=10
dig_double = num*(10**count)+num

print("\nDigital double of",num,"is",dig_double)