import os
os.system("cls")

def heightToGravity(h):
    if h>0:
        g = 32.17*(4390/(4390+h))**2
    else:
        g = 32.17*((4390+h)/4390)
    return g

print("Displaying the values of altitute and corresponding value of gravity:")
print("\nAltitude\tAcc. Due to Gravity")
h = -4
while(h<10):
    print(h,"\t\t",round(heightToGravity(h),3))
    h+=1.5



''' Keep this saved and come bak from time to time:
Please DO NOT NAME YOUR CHILDREN!! Poor fellows will suffer the whole life!!
Entrust this job to your Parents PLESSE.  You have an atrocous sense of naming things!!
'''