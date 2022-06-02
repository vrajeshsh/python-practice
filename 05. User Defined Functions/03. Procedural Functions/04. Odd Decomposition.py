import os
os.system("cls")

def oddDecompose(n):
    cnt, mult, end=0, "", n//3
    if n%2==0:
        print("\nThe number", n,"is even! Hence its odd decomposition is not possible.\n")
    else:
        for i in range(3, end+1, 2):
            if n%i==0 and i<(end-i):
                mult+="\n"+str(n)+" = "+str(i)+" x "+str(n//i)
                cnt+=1
        if cnt==0:
            print("\nThe number", n,"is prime! Hence its odd decomposition is not possible.\n")
        else:
            print("\nOdd decomposition for", n,":"+mult+"\n")

num = int(input("Enter an integer for odd decomposition: "))
oddDecompose(num)
