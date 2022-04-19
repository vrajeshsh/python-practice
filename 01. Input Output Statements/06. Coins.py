'''To calculate number of coins and total amount'''

print("To calculate number of coins and total amount:")
a = int(input("Enter the number of 50p coins: "))
b = int(input("Enter the number of 1re coins: "))
c = int(input("Enter the number of 2rs coins: "))
d = int(input("Enter the number of 5rs coins: "))
e = int(input("Enter the number of 10rs coins: "))
f = int(input("Enter the number of 20rs coins: "))

total_coins = a+b+c+d+e+f
total_amount = (a*0.5)+b+(c*2)+(d*5)+(e*10)+(f*20)

print("\nTotal number of coins :", total_coins,
	"\nTotal amount: ",round(total_amount))