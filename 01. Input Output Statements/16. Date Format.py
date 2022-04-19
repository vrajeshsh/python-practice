'''Represent 8-digit integer in valid short format date'''

print("To convert an 8-digit integer to a  valid short date:")
num = int(input("Enter the 8-digit integer: "))

yy = num%100
mm = (num//10000)%100
dd = (num//1000000)%100

print("\n",dd//10, dd%10,"-",mm//10, mm%10,"-",(yy%100)//10, (yy%100)%10, sep='')
