'''To calculate water tax based on usage code and gallons of water consumed'''

print("To calculate water tax based on usage code and usage of water:")
acc_num = int(input("Enter the account number: "))
code = input("Enter usage code [H/C/I]:").upper()
usage = float(input("Gallons of water used: "))

if code=='H':
	tax = 250 + 0.5 * usage
elif code=='C':
	tax = 1000 + 0.25 * (usage-1000)
elif code=='I':
	tax = 1500 if usage < 4000 else (2000 if usage <= 10000 else 3000)
else:
	tax = 0
	print("\nPlease check the usage code and try again!")

print("\nACCOUNT NO.\tUSE CODE\tWATER CONSUMED (usage)\tTAX AMOUNT (RS)\n",
	acc_num,"\t\t",code,"\t\t",usage,"\t\t\t",tax)
