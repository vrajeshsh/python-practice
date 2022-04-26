'''Generate all 3 digit numbers whose first 2 numbers are a factor of the last'''

print("Generate all 3 digit numbers whose first 2 numbers are a factor of the last")

facs=""
for i in range(100, 1000):
	dig = i%10
	temp = i//10
	if dig>1 and temp%dig==0:
		facs+= str(i) if facs=="" else ", "+str(i)

print("\n\nSuch numbers are: ", facs)
