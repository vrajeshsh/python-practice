print("To separate odd digits from even and find respective sums:")
num = int(input("Enter an integer: "))

temp,even,odd,e_sum,o_sum,dig=num,"","",0,0,0
while(temp>0):
    dig=temp%10
    if dig%2==0:
        even+=str(dig) if even=="" else ", "+str(dig)
        e_sum+=dig
    else:
        odd+=str(dig) if odd=="" else ", "+str(dig)
        o_sum+=dig
    temp//=10

if e_sum==0:
    print("\nNo even digits found in the integer!")
else:
    print("\nEven digits:\n",even,"\nSum:",e_sum)
if o_sum==0:
    print("\nNo odd digits found in the integer!")
else:
    print("\nOdd digits:\n",odd,"\nSum:",o_sum)
print("\n")
