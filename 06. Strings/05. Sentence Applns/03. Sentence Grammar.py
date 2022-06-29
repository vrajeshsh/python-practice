import os
os.system("cls")

def isendofsentence(para, pos):
    paralen = len(para)
    if pos==paralen-1:
        return True


def grammaticalStatus(pos):
    status = ""
    if para[pos]=="!":
        status = "Exclamatory"
    elif para[pos]=="?":
        status = "Interrogative"
    elif para[pos]
        

print("To display frequency of vowels, consonants, space and special characters in paragraph:")
para = input("Enter the paragraph:\n").strip()+"  "
paralen = len(para)

new_str, count, vow, con, dig, spc, spl = "", 0, 0, 0, 0, 0, 0
for i in range(paralen-2):
    
    if isendofsentence(para, i):
        count+=1

        new_str+="\n"+str(count)+". "+ para[i]
    else:
        new_str+=para[i]

print("\nSentences in the paragraph:\n",new_str,
        "\n\nList of different characters and their frequencies:",
            "\nVOW\tCON\tDIG\tSPC\tSPL\n",
                vow,"\t",con,"\t",dig,"\t",spc,"\t",spl,"\n",sep='')

'''
This one you please complete tomorrow after returning from the office.

Keep these facts about sentences in mind:
1. A sentence can be Negated if it has either of the words in it viz. no, never, not, neither
2. A sentence may be considered as affirmative if it has a yes word in it or even number of
negated words (already mentioned above)
3. Exclamatory and Interrogative you have already understood and done them.
4. If control does not fall in any category of the sentences, then it becomes a Statement.
'''