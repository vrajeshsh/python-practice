'''To prepare a frequency distribution table'''

print("To prepare a frequency distribution table:")
n = int(input("Enter number of students: "))

count1,count2,count3,count4=0,0,0,0
print()
for i in range(1,n+1):
    print("Enter Marks for student #",i,":",end='')
    num = float(input())
    if num<35:
        count1+=1
    elif num<60:
        count2+=1
    elif num<80:
        count3+=1        
    else:
        count4+=1

print("\nCATEGORY\tMARKS(%)\tFREQUENCY\nFail\t\t0-34\t\t",count1,
        "\nPass\t\t35-59\t\t",count2,
        "\nGood\t\t60-79\t\t",count3,
        "\nVery Good\t80-100\t\t",count4)


