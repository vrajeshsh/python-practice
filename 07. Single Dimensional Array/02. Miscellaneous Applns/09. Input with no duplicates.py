import os
from traceback import walk_stack
from xmlrpc.client import NOT_WELLFORMED_ERROR
os.system("cls")

print("To ensure no duplicates can be entered in array:")
n = int(input("Enter the number of marks: "))
print()

mks, i = [], 0
while i<n:
    print("Enter marks #", i+1,": ", sep='', end='')
    temp = int(input())
    if temp not in mks:
        mks.append(temp)
        i+=1
    else:
        print("Duplicate entry entered!")

print("\nThe list of marks:\n",mks,"\n",sep='')

# In your spare time think of doing this program in Java! And all this time when you would be
# solving the same program.... keep praising the creator of Python!!