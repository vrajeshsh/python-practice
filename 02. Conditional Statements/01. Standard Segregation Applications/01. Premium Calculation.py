'''To calculate the premium amount due'''

print("To calculate the premium amount due for an employee: ")
name = input("Enter name: ")
age = int(input("Enter age: "))
sal = float(input("Enter Salary: Rs "))

if age<20:
	prem = 0
elif age<=35:
	prem = .08*sal
elif age<=50:
	prem = .1*sal
else:
	prem = .14*sal

print("\n",name,"'s total insurance due: Rs ",prem, sep='')
