'''To calculate the Taxi fare based on distance travelled'''

print("To calculate the Taxi fare based on distance travelled:")
name = input("Enter name of user: ")
distance = float(input("Enter total distance travelled: "))

if distance <= 1:
	rate = 25
elif distance <= 6:
	rate = 25 + 10 * (distance - 1)
elif distance <= 12:
	rate = 25 + (10 * 5) + 15 * (distance - 6) 
elif distance <= 18:
	rate = 25 + (10 * 5) + (15 * 6)  + 20 * (distance - 12) 
else:
	rate = 25 + (10 * 5) + (15 * 6) + (20 * 6) + 25 * (distance - 18)

#rate = 25 if distance <= 1 else ((25 + 10 * (distance - 1)) if distance <= 6 else (25 + (10 * 5) + 15 * (distance - 6) if distance <= 12 else (25 + (10 * 5) + (15 * 6)  + 20 * (distance - 12)  if distance <= 18 else 25 + (10 * 5) + (15 * 6) + (20 * 6) + 25 * (distance - 18))))

print("\nNAME\t\t\tDISTANCE TRAVELLED\t\tCHARGE (RS)\n",
	name,"\t\t",distance,"\t\t\t\t",rate,sep='')
