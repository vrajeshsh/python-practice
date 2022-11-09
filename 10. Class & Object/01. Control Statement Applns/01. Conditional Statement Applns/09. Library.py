import os
os.system("cls")

class Library():
    def __init__(self, name, type, days):
        self.name = name
        self.type = type
        self.days = days

    def lateFine(self): # This way people used to code in 2000... but well in 22 years things have changed!!
        if self.days <= 10:
            fine = 3.5 * self.days if self.type.lower() == "t" else 5 * self.days
        elif self.days <= 15:
            fine = 3.5 * 10 + 5.5 * (self.days - 10) if self.type.lower() == "t" else 5 * 10 + 7.5 * (self.days - 10)
        elif self.days <= 30:
            fine = 3.5 * 10 + 5.5 * 5 + 7 * (self.days - 15) if self.type.lower() == "t" else 5 * 10 + 7.5 * 5 + 10 * (self.days - 10)
        else:
            fine = 3.5 * 10 + 5.5 * 5 + 7 * 15 + 10 * (self.days - 30) if self.type.lower() == "t" else 5 * 10 + 7.5 * 5 + 10 * 15 + 15 * (self.days - 10)

        return fine

    def display(self):
        print("\n\x1B[3mGlenhill City Library, Wall St, New Haven, CT 06511, USA\x1B[0m",
        "\nMember Name: ",self.name,
        "\nBook issued: ",("Genaral" if self.type.upper() =='G' else "Text"),
        "\nBook retained for: ",self.days,
        "\nLibrary Fine: $",self.lateFine(),"\n", sep='')

print("TO calculate late fine on a book: ")
name = input("Enter the name: ")
type = input("Enter type of book [T/G]: ")
days = int(input("Enter no. of days late: "))

obj = Library(name, type, days)
obj.display()

# But the style is very bad... In real-life we cannot work this way...
# unless you board a time machine and go in the future and come back  
# and complete what you had to complete in the past.

# Your approach... that is bad. Why write pass... and pass by...
# Go like real-life... as all of do... hard or easy lengthy or Tiring  
# we go forward understood sir