import os
os.system('cls')

class Time():
    def __init__(self, hh = 0, mm = 0):
        self.hh = hh
        self.mm = mm

    def input(self):
        self.hh = int(input("Enter hours: "))
        self.mm = int(input("Enter minutes: "))

    def display(self):
        print(self.to_string(), sep='', end='')

    def to_string(self):
        hh = str(self.hh) if self.hh>=10 else "0"+str(self.hh)
        mm = str(self.mm) if self.mm>=10 else "0"+str(self.mm)
        return hh + ":" + mm

    def is_valid(self):
        return 0 <= self.hh <=23 and 0<= self.mm <=59
    
    ''' Below code is WRONGLY DONE! It does not handle 'overnight timing' '''
    def time_diff(self, tm):
        return abs((self.hh*60+self.mm)-(tm.hh*60+tm.mm))

    def duration_to_string(self, tm):
        diff = self.time_diff(tm)
        hh = diff//60
        mm = diff%60
        hh = str(hh) if hh>=10 else "0"+str(hh)
        mm = str(mm) if mm>=10 else "0"+str(mm)
        return hh + ":" + mm

class Flight():
    def __init__(self, fl_name = "", fl_num = "", dt_time = Time(), arr_time = Time()):
        self.flight_name = fl_name
        self.flight_num = fl_num
        self.depart_time = dt_time
        self.arrive_time = arr_time

    def input(self):
        self.flight_name = input("Enter the name of flight: ")
        self.flight_num = input("Enter the flight number: ")
        print("Enter the departure time: ")
        self.depart_time.input()
        print("Enter the arrival time: ")
        self.arrive_time.input()

    def display(self):
        duration = self.depart_time.duration_to_string(self.arrive_time)
        print("\n",self.flight_name,"\t", self.flight_num,"\t",sep='', end='')
        self.depart_time.display()
        print("\t\t", sep='', end='')
        self.arrive_time.display()
        print("\t\t",duration, sep='', end='')

    def get_flight_name(self):
        return self.flight_name

    def get_flight_num(self):
        return self.flight_num

    def depart_time_to_string(self):
        return self.depart_time.to_string()

    def arrive_time_to_string(self):
        return self.arrive_time.to_string()

    def get_depart_time(self):
        return self.depart_time

    def get_arrive_time(self):
        return self.arrive_time

class FlightManager():
    def __init__(self):
        self.flights = []

    def fill_details(self):
        n = int(input("\nEnter the number of flights: "))
        for i in range(n):
            flight = Flight()
            print("\nEnter details for flight #",i+1,":", sep='')
            flight.input()
            self.flights.append(flight)

    def show_details(self):
        for flight in self.flights:
            flight.display()
        print()

    ''' The below function code also might not work. Need to fix it. '''
    def sort_details(self):
        return sort(self.flights, key = Flight.get_arrive_time().time_diff(Flight.get_depart_time()))

    ''' The below method code also needs to be completed. '''
    def search_details(self):
        pass

ch, obj = 0, FlightManager()
while ch!=4:
    print("\nWELCOME TO Indigo's Flight Portal",
        "\nChoose from the following:",
        "\n1. Add new flights",
        "\n2. Display flight details",
        "\n3. Query on flights",
        "\n4. Exit Application.")
    ch = int(input("Enter your choice (1 - 4): "))

    match(ch):
        case 1:
            print("To manage flight details and perform query on them:")
            obj.fill_details()
        case 2:
            print("\nThe list of flights as provided:",
                "\nName\t\tNumber\tDeparture Time\tArrival Time\tDuration", sep='')
            obj.show_details()
        case 3:
            obj.search_details()
        case 4:
            print("\nThank you for using Indigo's Flight Portal!\n")
        case _:
            print("\nIncorrect choice entered! Choose between 1 - 4 only!")

# Kindly keep this DONE. Will check tomorrow then.