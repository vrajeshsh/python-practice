'''To calculate ticket sales based on age category'''

print("To calculate ticket sales based on age category:")
n = int(input("Enter number of people: "))

price,count1,count2,count3,count4=0,0,0,0,0

print()
for i in range(1,n+1):
    print("Enter age of person #",i,": ",sep='',end='')
    age = float(input())
    if age<4:
        count1+=1
    elif age<=18:
        count2+=1
    elif age<=59:
        count3+=1
    else:
        count4+=1
        
price = count2*30+count3*40

print("\nCATEGORY\tNO. OF PEOPLE\nBelow 4\t\t",count1,
        "\n4-18\t\t",count2,
        "\n19-59\t\t",count3,
        "\nAbove 59\t",count4,
        "\n\nTotal Amount: Rs",price)   
# Remove the price calculation from each if check block and place it 
# somewhere else ONCE only