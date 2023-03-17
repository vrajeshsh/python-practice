import os
os.system("cls")

class TextEncoder():

    def getSentences(self):
        self.sent=[]
        self.n = int(input("Enter the number of sentences: "))
        print()
        if self.n<13:
            for i in range(1, self.n+1):
                print("Enter sentence #",i,": ", sep='', end='')
                self.sent.append(input())
        else:
            print("\nInvalid entry!\n", sep='')
            exit()
    ''' You are coding in 2022 for US IT companies. Make the below method code use only TWO LOOPS
        One i for the no. of sentences and one inner loop for handling the words...
    '''
    def encode(self):
        word, encoded = "", ""
        for i in range(self.n):
            if i%2==0:
                new_str=''
                for j in self.sent[i]:
                    new_str+=(chr(ord(j)-24) if j in "YyZz" else chr(ord(j)+2))if j.isalpha() else j
            else:
                new_str=''
                for j in self.sent[i]:
                    if j.isalnum() and self.sent[i].index(j)!=len(self.sent[i])-1:
                        word+=j
                    else:
                        new_str = word+j+new_str
                        word=""
            encoded+=new_str+"\n"
        return encoded

    def display(self):
        print("\nThe encoded sentences are:\n",self.encode(),"\n", sep='')

print("To changes characters in odd rows to two characters ahead and reverse the even sentences: ")

obj = TextEncoder()
obj.getSentences()
obj.display()

# ALWAYS in coding first PLAN OUT your task and approach...