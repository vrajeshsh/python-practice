'''To display all factors of an integer. Also find the mean, lowest and highest among them'''

print("To display the factors of an integer and also find the mean, max and min factors")
num = int(input("Enter an integer: "))

facs, fsum, count, mini = "", 0, 0, num

for i in range(2, num//2+1):
	if num%i== 0:
		fsum+=i
		count+=1
		maxi= i
		if i < mini:
			mini = i
		facs+= str(i) if fsum==i else ", "+str(i)

mean = round(fsum/count,3)

if facs == "":
	print("\nThe number ", num, " is Prime and does not have any true factor!", sep='')
else:
	print("\n\nThe factors of", num,"are: ", facs,
		"\nHighest Factor: ",maxi,
		"\nLowest Factor: ",mini,
		"\nMean of all factors: ",mean)

