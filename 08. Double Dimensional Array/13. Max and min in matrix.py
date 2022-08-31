import os
os.system("cls")

print("To find the Max and Min in a matrix and their positions:")
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
print()

num, max_pos, min_pos = [], "", ""

for i in range(r):
    _ = []
    for j in range(c):
        elem = int(input("Enter element for row #"+str(i+1)+" and column #"+str(j+1)+": "))
        _.append(elem)
    num.append(_)

print("\nThe elements of the 2-D array:")
for i in range(r):
    for j in range(c):
        print(num[i][j],"\t", end='')
    print()

maxi, mini = num[0][0], num[0][0]
for i in range(r):
    for j in range(c):
        if maxi < num[i][j]:   
            maxi = num[i][j]
            max_pos="("+str(i+1)+", "+str(j+1)+")"
        elif num[i][j]==maxi:
            max_pos+= ", ("+str(i+1)+", "+str(j+1)+")"
        if mini > num[i][j]:   
            mini = num[i][j]
            min_pos="("+str(i+1)+", "+str(j+1)+")"
        elif num[i][j]==mini:
            min_pos+=  ", ("+str(i+1)+", "+str(j+1)+")"
            
print("\nHighest element of the array: ",maxi,
    "\nPresent at location: ",max_pos,"\n\nLowest element of the array: ",mini,
    "\nPresent at locations: ",min_pos,"\n")

# The challenge in the program is to find the max and min and all their 
# locations using just one PAIR of loops   Sorry!!  Now try please...

#Plan out properly and then start coding the algorithm