import os
os.system("cls")

print("To display details of records based on part of their information:")
n = int(input("Enter the number of names: "))

names, numbers = [], []
for i in range(n):
    print("\nEnter details of record #",i+1,": ",sep='')
    names.append(input("Name: "))
    numbers.append(input("Number: "))

searchItem = input("\nEnter search item: ")
lgt = len(searchItem)
matches, count="", 0
for i in range(n):
    if names[i][:lgt].lower()==searchItem.lower() or \
        numbers[i][:lgt]==searchItem:
        matches+=names[i]+"\t\t\t"+numbers[i]+"\n"
        count+=1

if matches:
    print("\nSearch successful!\nThe matching records are:",
        "\nNAME\t\tPHONE NUMBERS\n",matches,
        "(",count," record(s) found)\n", sep='')
else:
    print("\nSearch unsuccessful!\n")
