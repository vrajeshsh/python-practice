import os
os.system('cls')

class Date:
    # Declaring class variables below
    month_names = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", 
        "Nov", "Dec"]
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, dd = 0, mm = 0, yy = 0):
        self.dd, self.mm, self.yy = dd, mm, yy
        # Using the class variable below
        Date.month_days[2] = 29 if self.yy%400==0 or (self.yy%100!=0 and self.yy%4==0) else 28

    def __str__(self):
        dd = "0"+str(self.dd) if self.dd<10 else str(self.dd)
        mm = Date.month_names[self.mm]
        yy = str(self.yy)[2:]
        return dd+"-"+mm+"-"+yy

    def input(self):
        self.dd = int(input("Enter the day [1 - 31]: "))
        self.mm = int(input("Enter the month [1 - 12]: "))
        self.yy = int(input("Enter the year: "))

    def is_valid(self):
        return 1000<=self.yy<=9999 and 1<=self.mm<=12 and 1<=self.dd<=Date.month_days[self.mm]

    def display(self):
        print(self.__str__(), sep='', end='') # Perhaps this line could generate a run-time error!!

    def get_date_number(self):
        mm = "0"+str(self.mm) if self.mm<10 else str(self.mm)
        dd = "0"+str(self.dd) if self.dd<10 else str(self.dd)
        return int(str(self.yy)+mm+dd)

    ''' The below method code needs to be CORRECTED using a single loop only. '''
    def date_difference(self, date):
        days1, days2 = self.dd+self.yy*365, date.dd+date.dd*365
        for i in range(1, self.mm):
            days1+=Date.month_days[i]
        for i in range(1, date.mm):
            days2+=Date.month_days[i]
        return abs(days1 - days2)

    def time_period_to_string(self, date):
        diff = self.date_difference(date)
        yy, mm, dd = diff//365, (diff%365)//30, (diff%365)%30
        return str(yy)+" year(s), "+str(mm)+" month(s) and "+str(dd)+" days(s)"

class StaffMember:
    def __init__(self, name = "", num = "", desig = "", sal = 0, dob = Date(), doj = Date()):
        self.member_name = name
        self.member_num = num
        self.desig = desig
        self.salary = sal
        self.birth_date = dob
        self.join_date = doj
        self.retire_date = self.find_retire_date()

    def input(self):
        self.member_name = input("Enter name: ")
        self.member_num = input("Enter number: ")
        self.desig = input("Enter designation: ")
        self.salary = float(input("Enter salary: Rs"))
        print("Enter date of birth: ", sep='')
        self.birth_date.input()
        print("Enter date of joining: ", sep='')
        self.join_date.input()

    def display(self):
        print("\n", self.member_name,"\t", self.member_num, "\t\t", self.desig, "\t", 
            self.salary,"\t\t", sep='', end = '')
        self.birth_date.display()
        print("\t", sep='', end='')
        self.join_date.display()
        print("\t", sep='', end='')
        self.find_retire_date().display()

    def find_retire_date(self):
        return Date(self.join_date.dd, self.join_date.mm, self.birth_date.yy+60)

class StaffOrganizer:
    def __init__(self):
        self.staffList = []

    def add_staff_members(self):
        n = int(input("\nEnter the number of members: "))
        for i in range(n):
            staff = StaffMember()
            print("\nEnter details for staff member #",i+1,":", sep='')
            staff.input()
            self.staffList.append(staff)

    def show_staff_members(self):
        for staff in self.staffList:
            staff.display()
        print()

    ''' The below method code should be done CORRECTLY as per program requirement. '''
    def sort_staff_members(self):
        return sort(self.staffList, key = StaffMember().join_date, reverse = True)

    def search_staff_members(self):
        count = 0
        query = input("\nEnter search query: ")
        range = query.split("-")
        for staff in self.staffList:
            if query in [staff.member_name, staff.member_num, staff.birth_date, staff.join_date, 
                staff.retire_date] or (len(range)==2 and int(range[0])<=staff.salary<=int(range[1])):
                if count==0:
                    print("\nThe matching list of staff members:",
                        "\nNAME\t\tNUMBER\t\tDESIGNATION\t\tSALARY (Rs.)\tDATE OF BIRTH\t\
                            DATE OF JOINING\tDATE OF RETIRMEMENT", sep='')
                staff.display()
                count+=1
        print("\n\n",count," match(es) found!", sep='')

print("To store details of staff and perform query:")
ch, obj = 0, StaffOrganizer()
while ch!=4:
    print("\nWELCOME TO XYZ INTERNATIONAL HOTELS",
        "\nChoose from the following:",
        "\n1. Add new staff member",
        "\n2. Display staff details",
        "\n3. Query on staff members",
        "\n4. Exit Application.")
    ch = int(input("Enter your choice (1 - 4): "))

    match(ch):
        case 1:
            obj.add_staff_members()
        case 2:
            print("\nThe list of staff members as provided:",
            "\nNAME\t\tNUMBER\t\tDESIGNATION\t\tSALARY (Rs.)\tDATE OF BIRTH\tDATE OF JOINING\t\
                DATE OF RETIRMEMENT", sep='')
            obj.show_staff_members()
        case 3:
            obj.search_staff_members()
        case 4:
            print("\nThank you.\n")
        case _:
            print("\nIncorrect choice entered! Choose between 1 - 4 only!")

''' When you sit to FIX, kindly fix that Date program who is pending from long...
I have given comments against the methods that need improvement/fixation '''

# At least try to complete the two pending programs on Object List.
