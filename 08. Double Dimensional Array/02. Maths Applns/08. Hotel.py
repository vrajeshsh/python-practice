import os
os.system("cls")

'''
Even in the display details method care needs to be taken to print the details of the 2-D and the  
names together while running two loops only for the room[][]...
'''
def showdetails(name, room): # Arrays are always names SINGULAR as one element is accessed at a time...
    if len(name)>0:
        print("\nCUSTOMER NAME\t\tROOM NO.\tFLOOR\tCABIN")
        for i in range(len(name)):
            print(name[i],"\t\t",room[i][0],"\t\t",room[i][1],"\t",room[i][2])
    else:
        print("\nNO booking has yet been made currently!")

'''
The room 2-D array basically represents the HOTEL in a way... 
Each row of the room[][] represents a floor of the hotel. So, if the first floor has 5 rooms,
then the room 2-D array will have room[0][0] = 101, room[0][1]= 102, etc. till room[0][4]= 105.
As and when customers visit, these room nos. get filled up gradually... till all the 4 floors x 5 rooms 
get filled up.
'''
def reserveroom(custname, name, room):
    pass

'''
In Query, the loops should follow the 2-D array in  
search for the match for room nos. The trick is in the 2-D array loops also you need to handle the  
1-D array name[] for a match in it (in case the user-input for query is a name.).
The rest is understandable -- if a match is found, then the name, floor, cabin and the room no. must  
be displayed and if not then a error message.  
''' 
def querycustomer(name, room, srchitem):
    cnt = 0
    for i in range(len(room)):
        if srchitem in name[i] or srchitem == str(room[i][0]):
            cnt+=1
            if cnt==1:
                print("\nSearch successful! The matching records are:",
                "\n\nCUSTOMER NAME\t\tROOM NO.\tFLOOR\tCABIN")
            print(name[i],"\t\t",room[i][0],"\t\t",room[i][1],"\t",room[i][2])
    if cnt == 0:
        print("\nNo matching record(s) found!\n")

floors = int(input("Enter the number of floors: "))
cabins = int(input("Enter the number of cabins: "))

print("\nWELCOME TO HOTEL METROPOLITANO INTERNATIONAL")
ch, name, room, room_no = 0, [], [[0]*cabins for i in range(floors)], 100

while ch!=3:
    print("\nHOTEL MENU OPTIONS",
    "\n1. Room reservation",
    "\n2. Customer Query",
    "\n3. Exit Program")
    ch = int(input("Enter your choice (1-3): "))
    if ch==1:

        if len(name) < floors*cabins:
            name = input("\nEnter the name of the customer: ")
            room_no=room_no+1 if int(str(room_no)[-1])<cabins else room_no+101-cabins
            name.append(name)
            room.append([room_no, int(str(room_no)[0]), int(str(room_no)[-1])])
            print("\nBooking successful! Hope you have a wonderful stay!")
        else:
            print("\nWe're sorry! No bookings are available at this moment!")
    elif ch==2:
        srchitem = input("Enter name or room no. to search: ")
        querycustomer(name, room, srchitem)
    
    elif ch==3:
        print("\nTHANK YOU! Hope you had a nice stay!\n")
    
    else:
        print("\nIncorrect option! Enter choice between 1 - 3 only!")

# Again UNDERSTANDING PROBLEM!!!!!!
# Got it sir, can you please check the rest but? If there are mistakes in understanding in that also  

# Its DISASTER spelled out in the entire program. 

# When You should have been solving MOSTLY THESE TYPES of programs for real depth purposes... 
# I shall have to compromise so as to not bring along the more difficult types in any assignment...  
# for again then this kind of DISASTER I shall have to face!!  

# You better REVAMP the entire program in the guidelines as provided above before each function.  

# SIRS can we start with recursion today?