'''To display digits of 4-digit integer separately'''

print("To display the digits of a 4-digit integer: ")
num = int(input("Enter the 4-digit integer: "))

u = num%10
t = (num//10)%10
h = (num//100)%10
th = (num//1000)%10

print("\nDigits of ",num,": ",th,", ",h,", ",t,", ",u, sep='')
