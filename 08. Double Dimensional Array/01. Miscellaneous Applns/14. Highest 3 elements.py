import os
os.system("cls")

print("To find the top 3 highest elements in a matrix and their positions:")
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
print()

num, max_pos, sec_max_pos, third_max_pos = [], "", "", ""

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

maxi,sec_max, third_max = 0, 0, 0
for i in range(r):
    for j in range(c):
        
        if  num[i][j] > maxi:  
            third_max = sec_max
            sec_max = maxi
            maxi = num[i][j]

            third_max_pos = sec_max_pos
            sec_max_pos = max_pos
            max_pos="("+str(i+1)+", "+str(j+1)+")"
            
        if sec_max<num[i][j] and num[i][j]!=maxi:
            third_max = sec_max
            sec_max = num[i][j]

            third_max_pos = sec_max_pos
            sec_max_pos = "("+str(i+1)+", "+str(j+1)+")"

        if third_max<num[i][j] and num[i][j]!=sec_max and num[i][j]!=maxi:
            third_max = num[i][j]

            third_max_pos = "("+str(i+1)+", "+str(j+1)+")"
            
print("\nHighest element is",maxi,"occurs at location",max_pos,
        "\nSecond-highest element is",sec_max,"occurs at location",sec_max_pos,
        "\nThird-highest element is",third_max,"occurs at location",third_max_pos,"\n")
