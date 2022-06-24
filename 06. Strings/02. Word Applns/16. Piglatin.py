import os
os.system("cls")

def toPiglatin(word): # Its here! Think -- what if... got it
    last = "AY" if word.isupper() else "ay"
    for i in range(len(word)):
        if word[i] in "AEIOUaeiou":
            return word[i:]+word[:i]+last
    return word+last

word, count, new_str= "", 0, ""

print("To covert sentence to Piglatin:")
sent = input("Enter the sentence:\n").strip()+" "

for ch in sent:
    if ch.isalnum():
        word+=ch
    elif word!="":
        count+=1
        new_str+= toPiglatin(word).title() if count==1 else\
             toPiglatin(word)
        new_str+=ch
        if ch!=" ":
            new_str+=" "
        word=""

print("\nConverted sentence:\n",new_str,"\n", sep='')

'''
This many students say:
Sir stays so busy with other students... we call... he comes hurriedly
looks at our code for a few seconds... finds our flaws in no time...
BACK CALCULATES and plans data in such a manner that it works on THAT
FLAW... and Oh God, CRASHES our codes... all that happening in seconds again.
'''
#this is true but im not understanding the error.. please give 5 mins
# But Dear all that takes a lot of experience and P A I N S.. I would solemnly say!!