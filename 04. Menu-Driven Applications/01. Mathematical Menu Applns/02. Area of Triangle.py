import os
os.system("cls")

choice = 0

while choice != 4:
    print("\nAREA OF TRIANGLE",
        "\nOptions available are:",
        "\n1. Right-angled Triangle",
        "\n2. Equilateral Triangle",
        "\n3. Scalene Triangle",
        "\n4. Exit Program")
    choice = int(input("Enter your choice (1-4): "))

    if choice==1:
        print("\nCalculating Area of a Right-angled Triangle\n")
        base = float(input("Enter base length: "))
        hgt = float(input("Enter height: "))
        area = 0.5*base*hgt
        print("Area of the Right-angled Triangle:", round(area,3),"\n")
        
    elif choice==2:
        print("\nCalculating Area of an Equilateral Triangle\n")
        side = float(input("Enter length any side: "))
        area = (1.732/4)*(side**2)
        print("Area of the Equilateral Triangle:", round(area,3),"\n")
        
    elif choice==3:
        print("\nCalculating Area of a Scalene Triangle\n")
        a = float(input("Enter length of side 1: "))
        b = float(input("Enter length of side 2: "))
        c = float(input("Enter length of side 3: "))
        s = (a+b+c)/2 
        if a+b>c and b+c>a and c+a>b:
            area = (s*(s-a)*(s-b)*(s-c))**0.5
            print("Area of the Scalene Triangle:", round(area,3),"\n")
        else:
            print("Triangle is NOT POSSIBLE with the given sides!")
    
    elif choice==4:
        print("\nThe program ends here. Thank You!\n")
    
    else:
        print("\nWrong choice entered! Enter choice betwee 1 - 4 only.\n")
