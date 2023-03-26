# Caution: I AM CODING IN 2022! 
import os
from tokenize import maybe
os.system("cls")

class PythaTriplet():
    def __init__(self, lim):
        self.lim = lim

    def isPythagorean(self, x, y, z):
        return x*x==y*y+z*z or y*y==x*x+z*z or z*z==x*x+y*y

    def findTriplets(self):
        x = 3
        print("\nNumber\tPythagorean Triplets")
        while x < self.lim:
            y = x+1
            z = y+1
            while not self.isPythagorean(x,y,z=y+1):
                y+=2
            print(x,"\t",x,", ",y,", ",z,sep="")
            x+=2
        print()

print("To find all Pythagorean Triplets of odd numbers between 1 and 'n':")
lim = int(input("Enter the limit: "))
obj = PythaTriplet(lim)
obj.findTriplets()

# Really you know Vrajesh, I get T I R E D  improving the code of   
# my students... They ALL WANT TO GO TO US, but nobody writes or even  
# try to write or even THINK like them... I am the poor fellow who while  
# in Kokata, Mamta Bengal, that I train for US!!! 

# And the consequence?
# They start off with CS Major...
# Right after the first Sem, convert the Major to Minor...
# After the 3rd Sem, drop off or opt out from CS!!

# End of story!!

# How to prevent this, tell me!!!

# Sir i'll improve this, just want to know if two loops are allowed 