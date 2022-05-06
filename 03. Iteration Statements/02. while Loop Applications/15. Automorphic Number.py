from ast import Or
from lib2to3.pgen2.token import DOUBLESTAR
import os
from traceback import walk_stack
from xml.dom import WrongDocumentErr
os.system("cls")

print("To check if a given number is Automorphic or not:")
num = int(input("Enter the integer: "))

temp, count= num, 0

while(temp>0):
    count+=1
    temp//=10

print("\nThe integer ",num," is ",
    "NOT " if num!=(num*num%(10**count)) else "", 
    "Automorphic\n",sep='')
