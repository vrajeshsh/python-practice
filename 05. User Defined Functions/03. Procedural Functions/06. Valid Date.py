import os, math

from pkg_resources import IMetadataProvider
os.system("cls")

def showDate(dd, mm, yy):
    mon = "January" if mm==1 else "Febuary" if mm==2 else "March" if mm==3 \
        else "April" if mm==4 else "May" if mm==5 else "June" if mm==6 \
        else "July" if mm==7 else "August" if mm==8 else "September" if mm==9 \
        else "October" if mm==10 else "November" if mm==11 else "December"
    d = dd%10
    suffix= "st" if d==1 and dd!= 11 else "nd" if d==2 and dd!=12 \
            else "rd" if d==3 and dd!= 13 else "th" 

    print("\n",dd,suffix,mon,", ",yy,"\n",sep='')

num = int(input("Enter a 7/8 digit integer to represent date: "))

yy = num%10000
mm = (num//10000)%100
dd = num//1000000
cnt = int(math.log10(num))+1

if cnt==7 or cnt==8:
    showDate(dd, mm, yy)
else:
    print("\nPlease enter a 7 or 8 digit number to show date.\n")

# Fix the suffix issue in this program.