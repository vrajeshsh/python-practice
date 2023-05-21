import os
os.system('cls')

class Date:
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, d = 0, m = 0):
        self.dd = d
        self.mm = m

    def input(self):
        self.dd = int(input("Enter the date (dd): "))
        self.mm = int(input("Enter the month (mm): "))

    def display(self):
        print(self.to_string(), sep='')

    def date_to_days(self):
        days = self.dd
        for i in range(1, self.mm):
            days+=Date.month_days[i]
        return days

    def get_date(self):
        if self.mm>=10:
            return self.dd*100+self.mm
        else:
            return self.dd*10+self.mm

    def to_string(self):
        dd = "0"+str(self.dd) if self.dd<10 else str(self.dd)
        mm = "0"+str(self.mm) if self.mm<10 else str(self.mm)
        return self.dd+"-"+self.mm

    def is_valid(self):
        return 1<=self.dd<Date.month_days[self.mm] and 1<=self.mm<=12

    def date_difference(self, dt):
        return abs(self.date_to_days()-dt.date_to_days())
            
class Time:
    def __init__(self, h, m):
        self.hr = h
        self.mn = m

    def input(self):
        self.hr = int(input("Enter hours (hh): "))
        self.mn = int(input("Enter minutes (mm): "))

    def display(self):
        print(self.to_string(),sep='')

    def is_valid(self):
        return 0<=self.hr<=23 and 0<=self.mn<=59

    def to_string(self):
        hr = str(self.hr) if self.hr>=10 else "0"+str(self.hr)
        mn = str(self.mn) if self.mn>=10 else "0"+str(self.mn)
        return hr+" : "+mn

    def set_time(self, h, m):
        self.hr = h
        self.mn = m

    def time_to_minutes(self):
        return self.hr*60+self.mn

    def time_difference(self, tm):
        mins1, mins2 = self.hr*60+self.mn, tm.hr*60+tm.mn
        mins2+= 24*60 if mins2 < mins1 else 0
        return mins2 - mins1

class InternetUser:
    def __init__(self, u_id = "", login_dt = Date(), login_tm = Time(), logout_dt = Date(), logout_tm = Time()):
        self.user_id = u_id
        self.login_date = login_dt
        self.login_time = login_tm
        self.logout_date = logout_dt
        self.logout_time = logout_tm
        self.duration = self.get_duration()

    def input(self):
        self.user_id = input("Enter User Identification Number: ")
        print("Enter the login date: ")
        self.login_date.input()
        print("Enter the login time: ")
        self.login_time.input()
        print("Enter the logout date: ")
        self.logout_date.input()
        print("Enter the logout time: ")
        self.logout_time.input()

    ''' Need to work on the below code'''
    def calc_duration():
        time1 = 24*60 - self.login_time.time_to_minutes()
        time2 = self.logout_time.time_to_minutes
        date_diff = self.login_date.date_difference(self.logout_date)
        return date_diff*24*60+time1+time2

    def get_duration():
        return self.calc_duration()

    def display(self):
        print("\n", self.user_id, "\t",sep='', end='')
        self.login_date.display()
        print( "\t",sep='', end='')
        self.login_time.display()
        print( "\t",sep='', end='')
        self.logout_date.display()
        print( "\t",sep='', end='')
        self.logout_time.display()
        print( "\t",sep='', end='')
        self.duration.display()

class InternetUsage:
    def __init__(self, users=[]):
        self.users = users

    def add_records(self, n):
        for i in range(n):
            user = InternetUser()
            print("\nEnter details for user #",i+1,":", sep='')
            user.input()
            user.calc_duration()
            self.users.append(user)

    def show_records(self):
        ''' A heading is required here. '''
        for user in self.users:
            user.display()
        print()

    ''' Change the algorithm used below. Do not even think of sorting the records! Just find the 
        max duration, and then display the records having the same max duration. '''
    def show_top_users(self):
        for i in range(len(self.users)):
            for j in range(i+1, len(self.users)):
                duration1 = self.users[i].get_duration()
                duration2 = self.users[j].get_duration()
                if duration1<duration2:
                    self.users[i], self.users[j] = self.users[j], self.users[i]

    ''' The range-check is still MISSING! Kindly put that in the below code whenever free. '''
    def query_on_users(self, query_item):
        count = 0
        for user in self.users:
            if query_item in [users.user_id] or \
                query_item in [user.login_date.to_string(), user.logout_date.to_string(), 
                user.login_time.to_string(), user.logout_time.to_string()]:
                if count==0:
                    print("\nTher matching list of users:",
                    "\nUSER ID\tLOGIN DATE\tLOGIN TIME\tLOGOUT DATE\tLOGOUT TIME\tDURATION", sep='')
                user.display()
                count+=1
        print("\n\n",count," match(es) found!", sep='')

ch, obj = 0, InternetUsage()
while ch != 5:
    print("\nWelocome to XYZ Internet Services",
        "\nChoose from the following:",
        "\n1. Add Internet User(s)",
        "\n2. Display Usage Details",
        "\n3. Display Top Users",
        "\n4. Query on Users",
        "\n5. Exit Application.")
    ch = int(input("Enter your choice (1 - 5): "))

    match(ch):
        case 1:
            print("To manage user details and perform queries:")
            n = int(input("Enter the number of users to add: "))
            obj.add_records(n)
        case 2:
            print("\nThe list of users as provided:",
            "\nUSER ID\tLOGIN DATE\tLOGIN TIME\tLOGOUT DATE\tLOGOUT TIME\tDURATION", sep='')
            obj.show_records()
        case 3:
            print("\nThe list of top users:",
            "\nUSER ID\tLOGIN DATE\tLOGIN TIME\tLOGOUT DATE\tLOGOUT TIME\tDURATION", sep='')
            obj.show_top_users()
        case 4:
            query_item = input("Enter item to query on: ")
            obj.query_on_users(query_item)
        case 5:
            print("\nThank you!\n")
        case _:
            print("\nIncorrect choice entered! Choose between 1 - 5 only.")

# Kindly keep it COMPLETED for tomorrow. 