from itertools import combinations_with_replacement
import os
os.system("cls")

print("To arrange list in alphabetical order of country names and perform search:")
n = int(input("Enter number of countries: "))

countries, capitals = [], []
for i in range(n):
    print("\nEnter record #",i+1,": ",sep='')
    countries.append(input("Country: "))
    capitals.append(input("Capital: "))

search_str = input("\nSearch for: ")
lgt = len(search_str)
print("The given list of countries and their capitals:\n#\tCOUNTRY\t\tCAPITAL")
for i in range(n):
    print(i+1,"\t",countries[i],"\t\t",capitals[i])

# combi-sorting the two lists below where 'zip' zips the two lists as one and 
# the '*' unpacks them at the end back to the respective lists
# what if we wanted to sort basis of capitals? Reverse the order of the lists. The sorting is done as per the first list

countries, capitals = zip(*sorted(zip(countries, capitals))) 

print("\nThe list after arranged in alphabetical order of country names:\n#\tCOUNTRY\t\tCAPITAL")
for i in range(n):
    print(i+1,"\t",countries[i],"\t\t",capitals[i])

matches = ""
for i in range(n):
    if countries[i][:lgt].lower()==search_str.lower():
        matches+=str(i+1)+"\t"+countries[i]+"\t\t"+capitals[i]+"\n"

if matches:
    print("\nSearch successful!\nThe matching records are:",
        "\n#\tCOUNTRY\t\tCAPITAL\n",matches, sep='')
else:
    print("\nSearch unsuccessful!\n")

'''
There are two lists which you need to sort such that both the lists stay in sync. Shows, that you
need combi-sort here.
That is you need to combine the two lists while you sort and then un-combine them back to the lists
separately...
And however complicated it might sound... since the language is Python, we need to do all these in
a singleline statement.
But the million dollar question is: How do we do this?
'''

