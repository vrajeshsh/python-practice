import os
os.system('cls')

class VideoDisc():
    def __init__(self):
        self.name = ""
        self.type = ""
        self.price = 0.0 
        self.serialNo = self.copies = 0

    def accept(self):
        self.serialNo = int(input("Enter Serial Number: "))
        if self.serialNo==0:
            return 0
        self.name = input("Enter movie name: ")
        self.type = input("Enter genre: ")
        self.price = float(input("Enter price: "))
        self.copies = int(input("Enter number of copies: "))

    def show(self):
        print(self.serialNo,"\t", self.name,"\t\t", self.type, "\t$", self.price,"\t", self.copies,sep='')

    def get_copies(self):
        return self.copies

class VideoLibrary():

    def __init__(self):
        self.discs = []

    def store_details(self):
        n = int(input("Enter number of video discs: "))
        for i in range(n):
            disc = VideoDisc()
            print("\nEnter details for Disc #", i+1,": ", sep='')
            disc.accept()
            self.discs.append(disc)

    def show_details(self):
        for disc in self.discs:
            disc.show()

    def arrange_details(self):
        self.discs = sorted(self.discs, key=VideoDisc.get_copies, reverse = True)
        self.show_details()
        
    def show_special_discs(self):
        maxi, mini = VideoLibrary(), VideoLibrary()
        for disc in self.discs:
            copy = disc.get_copies()
            if copy==self.discs[0].get_copies():
                maxi.discs.append(disc)
            if copy==self.discs[-1].get_copies():
                mini.discs.append(disc)

        print("\nThe details of video disc having maximum copies:\n\nSerial No.\tMovie Name\t\tGenre\tPrice\tCopies", sep='')
        maxi.show_details()
        print("\nThe details of video disc having minimum copies:\n\nSerial No.\tMovie Name\t\tGenre\tPrice\tCopies", sep='')
        mini.show_details()
        
print("To arrange video discs in descending order and calculate max-min:")

obj = VideoLibrary()
obj.store_details()

print("\nSerial No.\tMovie Name\t\tGenre\tPrice\tCopies", sep='')
obj.show_details()

print("\nThe list of video discs after arranging as per number of copies:\n\nSerial No.\t\
    Movie Name\t\tGenre\tPrice\tCopies", sep='')
obj.arrange_details()

obj.show_special_discs()
print()

# First change. Then prepare sample test data and keep it the same way as yesterday.abs(  
# # Will run this program to see how it runs after that.)