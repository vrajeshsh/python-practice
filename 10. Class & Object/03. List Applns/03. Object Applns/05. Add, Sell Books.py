import os
os.system("cls")

class Book():
    def __init__(self):
        self.title = self.author = self.publisher = ""
        self.price = self.copies = 0

    def input(self):
        self.title = input("Enter Book title: ")
        self.author = input("Enter author name: ")
        self.publisher = input("Enter publisher name: ")
        self.copies = int(input("Enter number of copies: "))
        self.price = float(input("Enter price: "))

    def display(self):
        print(self.title,"\t",self.author,"\t",self.publisher,"\t\t",self.copies,"\t",self.price, 
            sep='')

    def get_copies(self):
        return self.copies

    def set_copies(self, c):
        self.copies= c

class Bookstore():
    def __init__(self):
        self.booklist = []

    def add_books(self):
        n = int(input("\nEnter the number of books to add to the store: "))
        for i in range(n):
            print("\nEnter details of book #", i+1, ": ", sep='')
            book = Book()
            book.input()
            self.booklist.append(book)

    def show_books(self):
        print("\nThe list of books available in the store:", 
            "\nTitle\t\t\t\tAuthor\t\t\tPublisher\t\t\tCopies\tPrice", sep='')
        for book in self.booklist:
            book.display()

    def get_index(self, title, author):
        i= 0
        for book in self.booklist:
            if book.title.lower()==title.lower() and book.author.lower()==author.lower():
                return i
            i+= 1
        return -1

    def is_sellable(self, title, author, copies):
        ind = self.get_index(title, author)
        if ind!=-1 and self.booklist[ind].copies>=copies:
            return True
        return False

    def sell_books(self, title, author, copies):
        ind = self.get_index(title, author)
        book = self.booklist[ind]
        if ind==-1:
            print("\nBook with given title and author NOT found!")
        elif not self.is_sellable(title, author, copies):
            print("\nSorry, the store currently has only ", self.booklist[ind].copies, " copies of ", title,"!", sep='')
        else:
            print("\nINVOICE\n\nTITLE\t\t\t\tCOPIES\tTOTAL\n",title,"\t",copies,"\t", copies*self.booklist[ind].price,sep='')
            book.set_copies(book.copies-copies)

print("To add and sell books in a bookstore:")

ch, obj = 0, Bookstore()
while ch!=4:
    print("\nWELCOME TO ABC BOOKSTORE",
    "\nChoose from the following:",
    "\n1. Add Book(s)",
    "\n2. Display book details",
    "\n3. Sell Book(s)",
    "\n4. Exit program.")
    ch = int(input("Enter your choice (1 - 4): "))
    
    match(ch):
        case 1:
            obj.add_books()
        case 2:
            obj.show_books()
        case 3:
            print("\nEnter details of book to be purchased: ")
            t_search = input("Enter title: ")
            a_seach = input("Enter author name: ")
            c_search = int(input("Enter number of copies: "))
            obj.sell_books(t_search, a_seach, c_search)      
        case 4:
            print("\nThank you!\n")
        case _:
            print("\nIncorrect choice entered. Choose between 1 - 4 only!")

# If you have time, then IMPROVE the presentation and layot of the output...
# Later when you will be doing Python programming with data files and csv files etc., your 
# presentation skills will be noticed by many!!

# So....
# OKay sir