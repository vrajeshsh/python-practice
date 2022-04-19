'''To calculate the Net Salary of a user'''

print("To calculate Net Salary of an employee:")
salary = float(input("Enter Basic Salary: Rs "))

da = 0.42*salary
hra = 0.12*salary
gross = salary + da + hra
it = 0.1*gross
pf = 0.12*gross
net = gross-it - pf

print("\nNet Salary: Rs ", round(net,3))