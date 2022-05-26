import os
os.system("cls")

def formNumbers(num):
    even, odd, even_cnt, odd_cnt = 0, 0, 0, 0 
    while(num>0):
        dig = num%10
        if dig%2==0:
            even+= (dig*(10**even_cnt))
            even_cnt+=1
        else:
            odd+=(dig*(10**odd_cnt))
            odd_cnt+=1
        num//=10

    print("\nEven-digit number: ",even,"\nOdd-digit number: ", odd,"\n",sep='')

num = int(input("Enter an integer to form even and digut numbers from it: "))
formNumbers(num)