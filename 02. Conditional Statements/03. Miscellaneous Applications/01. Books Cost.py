'''To calculate total cost of books based on number of copies purchased'''

print("To calculate total cost of books based on no. of copies purchased:")
book1 = int(input("Enter number of copies of 'God's Angels': "))
book2 = int(input("Enter number of copies of 'Jungle Kings': "))


if book1 + book2 >= 12:
	amt = (book1 + book2)*125
elif book1 + book2 >= 3:
	amt = (book1 + book2)*150
elif book1==1 and book2==1:
	amt = 300
else:
	amt = book1 * 125.5 + book2 * 220.75

print("\nThe total cost of the two books:\nRs ",amt)


