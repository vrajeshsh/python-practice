'''Generate all 3 digit numbers whose first 2 numbers are a factor of the last'''

print("Generate all 3 digit numbers whose first 2 numbers are a factor of the last")

facs=""


for i in range(100,1000):
	temp=i
	dig3 = temp%10

	dig2 = (temp//10)%10
	dig1 = (temp//100)
	if dig3 and dig2 and dig1>0 and dig3%dig2==0 and dig3%dig1==0:
		facs+= str(i) if i==111 else ", "+str(i)

print("\n\nSuch numbers are: ", facs)