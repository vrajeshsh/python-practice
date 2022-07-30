import os
os.system("cls")

print("To display records in descending order or marks and also search average: ")
ch, names, sub1mks, sub2mks, sub3mks, avgs = 0, [], [], [], [], []
while ch!=4:
    print("\nSELECT OPERATION FROM MENU",
        "\n1. Add new student(s) details",
        "\n2. Display student record(s)",
        "\n3. Search for student record(s)",
        "\n4. Exit Program")
    ch = int(input("Enter choice [1 - 4]: "))
    print()
    if ch==1:
        name = input("Enter name: ")
        sub1mk = int(input("Enter marks in subject 1: "))
        sub2mk = int(input("Enter marks in subject 2: "))
        sub3mk = int(input("Enter marks in subject 3: "))
        avg = round((sub1mk+sub2mk+sub3mk)/3,2)
        names.append(name)
        sub1mks.append(sub1mk)
        sub2mks.append(sub2mk)
        sub3mks.append(sub3mk)
        avgs.append(avg)
    elif ch==2:
        while sub_ch!=4:
            print("\nSELECT OPERATION FROM MENU",
            "\n1. Display the original records",
            "\n2. Display as per alphabetical order of names",
            "\n3. Display as per descending order of avergae(%) marks",
            "\n4. Exit to Main Menu")
        sub_ch = int(input("Enter choice [1 - 4]: "))
        print()
        res1, res2, res3, lgt = "", "", "", len(names)
        if sub_ch==1:
            print("The details of the given list of students:")
            for i in range(lgt):
                res1+=str(i+1)+"\t"+names[i]+"\t\t"+str(sub1mks[i])+\
                    "\t\t"+str(sub2mks[i])+"\t\t"+str(sub3mks[i])+\
                        "\t\t"+str(avgs[i])+"\n"
            print("\n#\tNAME\t\tSUB 1\t\tSUB 2\t\tSUB3\t\tAVG(%)\n",res1,sep='')
        elif sub_ch==2:
            print("The list of students arranged as per alphabetical order of names:")
            names, sub1mks, sub2mks, sub3mks, avgs = zip(*sorted(zip(names, sub1mks, sub2mks, sub3mks, avgs)))
            for i in range(lgt):
                res2+=str(i+1)+"\t"+names[i]+"\t\t"+str(sub1mks[i])+\
                    "\t\t"+str(sub2mks[i])+"\t\t"+str(sub3mks[i])+\
                        "\t\t"+str(avgs[i])+"\n"
            print("\n#\tNAME\t\tSUB 1\t\tSUB 2\t\tSUB3\t\tAVG(%)\n",res2,sep='')  
        elif sub_ch==3:
            print("The list of students arranged as per descending order of average(%) marks:")         
            avgs, names, sub1mks, sub2mks, sub3mks = zip(*sorted(zip(avgs, names, sub1mks, sub2mks, sub3mks), reverse = True))
            for i in range(lgt):
                res3+=str(i+1)+"\t"+names[i]+"\t\t"+str(sub1mks[i])+\
                    "\t\t"+str(sub2mks[i])+"\t\t"+str(sub3mks[i])+\
                        "\t\t"+str(avgs[i])+"\n"
            print("\n#\tNAME\t\tSUB 1\t\tSUB 2\t\tSUB3\t\tAVG(%)\n",res3,sep='')
        
    elif ch==3:
        search_str = input("Search for: ")
        lgt, len_str, matches = len(names), len(search_str), ""
        if search_str.isalpha():
            for i in range(lgt):
                if names[i][:len_str].lower()==search_str.lower():
                    matches+=str(i+1)+"\t"+names[i]+"\t\t"+str(sub1mks[i])+\
                        "\t\t"+str(sub2mks[i])+"\t\t"+str(sub3mks[i])+\
                        "\t\t"+str(avgs[i])+"\n"
        else:
            start_lim = int(search_str[:2])
            end_lim = int(search_str[3:])
            for i in range(lgt):
                if start_lim<=avgs[i]<=end_lim:
                    matches+=str(i+1)+"\t"+names[i]+"\t\t"+str(sub1mks[i])+\
                        "\t\t"+str(sub2mks[i])+"\t\t"+str(sub3mks[i])+\
                        "\t\t"+str(avgs[i])+"\n"
        if matches:
            print("\nSearch successful! The recordes matching the search item '",search_str,"' are:\n", sep='')
            print("\n#\tNAME\t\tSUB 1\t\tSUB 2\t\tSUB3\t\tAVG(%)\n",matches,sep='')
        else:
            print("\nSearch unsuccessful!")
    elif ch==4:
        print("End.\n")
    else:
        print("Wrong choice entered! Enter choice between 1- 4 only.\n")

'''
Update the above code by adding the following features which would also streamline it:
1. Make the display option have a sub-menu having the following options:
    1. Display the original records
    2. Display as per alphabetical order of names
    3. Display as per descending order of avergae(%) marks
    4. Exit to Main Menu
2. Add the following functions:
    display()   # Make provision to prine 'live' without any string
    getsorted(array1, array2, ...., ...., order) # sorts the arrays alphabetically if order==1 else as per average(%)
3. Make the search routine in one one loop under one block traversing the array(s) ONLY ONCE. For this,
   P L A N  properly.


Don't know why -- (perhaps due to lack of time) you do not cover up backlogs at all...
No problem. I stay very busy managing the world of students and family...
Still I PROMISE, if by 31st night, you do not patch up. I WILL PATCH UP everything P R O P E R L Y
for you. At least spend some time to learn from the codes... 
'''