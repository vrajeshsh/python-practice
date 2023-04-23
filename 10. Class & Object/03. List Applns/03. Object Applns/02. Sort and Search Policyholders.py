import os
os.system("cls")

class PolicyHolder():
    def accept(self):
        name = input("Enter name: ")
        if name == "":
            return 0
        policy_num = int(input("Enter Policy Number: "))
        premium = int(input("Enter the premium: "))
        time = int(input("Enter time (in years) for maturity: "))

    def display(self):
        print(self.policy_num,"\t", self.name, "\t", self.premium, "\t", self.time, sep='')

    def arrange(holders):
        sort(holder, key=self.policy_num)

    def search(holders):
        pass

print("To search for a policy holder on basis of policy number, enter 'esc' in 'Name' to exit: ")
i, holders = 1, []
while True:
    print("\nEnter details for policy holder #", i, ": ", sep='')
    policy = PolicyHolder().accept()
    if policy == 0:
        break
    holder = PolicyHolder()
    #holders.append(holder.name, holder.policy_num, holder.premium, holder.time)
    i+=1

print(Polic)
print("\nThe given list of policy holders: ")
print("\nPolicy Number\tName\t\tPremium\tMaturity (in years)")
for holder in holders:
    holder.display()

print("\nPolicies in Ascending order of policy number: ")
print("\nPolicy Number\tName\t\tPremium\tMaturity (in years)")
arrange(holders)
