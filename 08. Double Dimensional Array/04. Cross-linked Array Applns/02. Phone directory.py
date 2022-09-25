import os
os.system("cls")

searchVal = "\0"

n = int(input("Enter number of records to be stored: "))

directory = [[""]*3 for i in range(n)]

for i in range(n):
    print("\nEnter the details for record #",(i+1),":", sep='')
    directory[i][0] = input("Enter name: ")
    directory[i][1] = input("Enter address: ")
    directory[i][2] = input("Enter phone number: ")

print("\nThe list of records as stored in the directory:",
    "\nNAME\t\t\tADDRESS\t\t\tPHONE NUMBER")
for i in range(n):
    print(directory[i][0],"\t\t",directory[i][1],"\t\t", directory[i][2], sep='')

while searchVal != "":
    searchVal = input("\nEnter the search item [Press 'Enter' key to STOP]: ")
    if searchVal == "":
        print("\nThe program ends here. Thank You!")
        continue
    cnt= 0    
    for i in range(n):
        if searchVal.lower() in directory[i][0].lower() or searchVal in directory[i][2]:
            cnt+=1
            if cnt==1:
                print("\nSearch successful! The details of the matching record(s) given below:",
                    "\nNAME\t\t\tADDRESS\t\t\tPHONE NUMBER")
            print(directory[i][0],"\t\t",directory[i][1],"\t\t", directory[i][2],sep='')
    if cnt==0:
        print("\nNo matching records found!\n")
    else:
        print("\n(",cnt," record(s) found.)\n", sep='')
