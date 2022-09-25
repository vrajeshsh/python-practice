import os
os.system("cls")

month, cnt = [["January", "31"], ["February", "28"], ["March","31"], ["April", "30"], 
    ["May","31"], ["June","30"], ["July","31"], [ "August","31"],[ "September", "30"],
    ["October", "31"],["November", "30"],["December","31"]], 0

print("\nThe details of the months are given below:",
    "\nMONTH #\t\tMONTH NAME\tDAYS IN MONTH")
for i in range(12):
    print((i+1), "\t\t",month[i][0],"\t\t", month[i][1],sep='')

searchVal = input("\nEnter the month number, month name, or days to search for: ")

for i in range(12):
    if searchVal.title() in month[i][0] or searchVal==str(i+1) or searchVal==month[i][1]:
        cnt+=1
        if cnt==1:
            print("\nSearch successful! the matching record(s) are as follows:",
                "\nMONTH #\t\tMONTH NAME\tDAYS IN MONTH")
        print((i+1),"\t\t",month[i][0],"\t\t",month[i][1])

if cnt==0:
    print("\nNo matching records found!\n")
else:
    print("\n(",cnt," record(s) found.)\n", sep='')
