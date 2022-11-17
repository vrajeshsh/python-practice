import os
os.system("cls")

class Name():
    def __init__(self, n):
        self.name = n
    
    def display(self):
        print("\nInitials: ",self.initials(),
            "\nShort Name: ", self.shortName(),"\n",sep='')

    def initials(self):
        ini = ""
        for i in range(len(self.name)):
            if self.name[i].isalpha() and (i==0 or self.name[i-1]==" "):
                ini+= self.name[i].upper()+"."
        return ini

    def shortName(self):
        short= self.initials()[:-1]
        surname = self.name[self.name.index(short[-1])+1:]
        ''' Try at (alternate) home to do the below portion WITHOUT ANY LOOP. You appear to be
        pretty CONFIDENT in Strings -- So... should try.
        
        [ But Alas perhaps this confidence could be shortlived -- Who knows!!]
        '''
        return short+surname.lower()

print("To display the initials and shortname of the user: ")
name = input("Enter the name: ")

obj = Name(name)
obj.display()

''' Problems found are as follows:
1. OOPS principles NOT FOLLOWED. Fix it.
2. This program will CRASH if names are given in all caps or lowercase.
'''