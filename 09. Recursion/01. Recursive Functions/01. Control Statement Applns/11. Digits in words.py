import os
os.system("cls")

def digitsinwords(n):
    if n==0:
        return ""
    return  digitsinwords(n//10)+words[n%10]+" "

words=["zero","one","two", "three","four","five","six","seven","eight","nine"]
print("To display the digits of a given input in words:")
n = int(input("Enter the number: "))

print("\n",n," in words: ",digitsinwords(n),"\n", sep='')