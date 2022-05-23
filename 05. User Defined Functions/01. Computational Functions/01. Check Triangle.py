from distutils.dir_util import remove_tree
import os
os.system("cls")

def getType(a, b, c):
    type=""
    if a==90 or b==90 or c==90:
        type = "Right-angled "
    elif a>90 or b>90 or c>90:
        type = "Obtuse-angled "
    else:
        type = "Acute-angled "
    if a == b == c:
        type+= "Equilateral"
    elif a==b or b==c or c==a:
        type+="Isosceles"
    else:
        type+="Scalene"
    return type

print("To find the type of a triangle:")
a = float(input("Enter angle 1: "))
b = float(input("Enter angle 2: "))
c = float(input("Enter angle 3: "))

if a+b+c == 180:
    print("\nTriangle type:",getType(a,b,c),"\n")
else:
    print("\nThe given angles do not form a VALID triangle!")