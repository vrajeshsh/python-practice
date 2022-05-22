import os
os.system("cls")

def digToWord(dig):
    return "Zero" if dig==0 else "One" if dig==1 \
        else "Two" if dig==2 else "Three" if dig==3 \
        else "Four" if dig==4 else "Five" if dig==5 \
        else "Six" if dig==6 else "Seven" if dig==7 \
        else "Eight" if dig==8 else "Nine"

print("To covert digits of an integer to words:")
temp = num = int(input("Enter an integer: "))
word=""
while temp>0:
    word= digToWord(temp%10)+" "+ word  # string formed through 'reverse concatenation'
    temp//=10

print("\n",num,"in words:",word,"\n")
