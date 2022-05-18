import os
os.system("cls")

choice = 0

while choice != 4:
    print("\nVOLUME OF GEOMETRICAL FIGURES",
        "\nOptions available are:",
        "\n1. Volume of a Cube",
        "\n2. Volume of a Sphere",
        "\n3. Volume of a Cuboid",
        "\n4. Exit Program")
    choice = int(input("Enter your choice: "))
    
    if choice==1:
        print("\nCalculating Volume of a Cube\n")
        side = float(input("Enter length of any equal side: "))
        vol = side**3
        print("Volume of the Cube:", round(vol,3),"\n")

    elif choice==2:
        print("\nCalculating Volume of a Sphere\n")
        rad = float(input("Enter length of radius: "))
        vol = (88/21)*(rad**3)
        print("Volume of the Sphere:", round(vol,3),"\n")

    elif choice==3:
        print("\nCalculating Volume of a Cuboid\n")
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        h = float(input("Enter height: "))
        vol = l*b*h
        print("Volume of the Cuboid:", round(vol,3),"\n")
    
    elif choice==4:
        print("\nThe program ends here. Thank You!\n")
    
    else:
        print("\nWrong choice entered! Enter choice betwee 1 - 4 only.\n")
