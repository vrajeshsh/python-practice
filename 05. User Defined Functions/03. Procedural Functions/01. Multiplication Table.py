import os
from readline import write_history_file
os.system("cls")

def showTableOf(n):
    print("\nMULTIPLICATION TABLE OF", n)
    for i in range(1, 13):
        print(n,"x",i,"=",n*i)

start = int(input("Enter the starting limit: "))
end = int(input("Enter the ending limit: "))

print("\nThe multiplication tables for the range", start,"-", end)
for i in range(start, end+1):
    showTableOf(i)
print()
'''
This Python's function WITHOUT return -- the void type functions
where we just do the job abd done. That is exactly the reason write_history_file
the names of such functions are often VERBS due to the action - orintation
'''