import os
os.system("cls")

# def expntopoly(polyexpn):

#  pass

    

def sumOfPolynomials(poly1, poly2):
    res = []
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            if poly1[i][1]==poly2[j][1]:
                res.append( [poly1[i][0]+poly2[j][0], poly1[i][1]])
                del poly2[j]
                break
        else:
            res.append( [poly1[i][0], poly1[i][1]])

    res.append(poly2)
    return res

def diffOfPolynomials(poly1, poly2):
    res = []
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            if poly1[i][1]==poly2[j][1]:
                res.append( [poly1[i][0]-poly2[j][0], poly1[i][1]])
                del poly2[j]
                break
        else:
            res.append( [poly1[i][0], poly1[i][1]])

    res.append(poly2)
    return res

# The below function converts the magnitudes and the coefficients of the poly 2-D array into an expn
def polytoexpn(poly):
    expn = ""
    for i in range(len(poly)):
        expn+=str(poly[i][0])+"x^"+str(poly[i][1])
    return expn        

print("To perform addition and subtraction of polynomials:")
# polyexpn1 = input("Enter first polynomial:\n")
# polyexpn2 = input("Enter second polynomial:\n")

# poly1= expntopoly(polyexpn1)
# poly2= expntopoly(polyexpn2)

n1= int(input("Enter the number of terms in the first polynomial: "))
n2= int(input("Enter the number of terms in the second polynomial: "))

poly1, poly2 = [[0]*2 for i in range(n1)], [[0]*2 for i in range(n1)]

print("\nFor the First Polynomial, enter the details of the", n1,"terms below:")
for i in range(n1):
    print("\nEnter the details of Term # ", i+1,": ", sep='')
    poly1[i][0]= int(input("Enter the magnitude: "))
    poly1[i][1]= int(input("Enter the coefficient: "))
print("\nFor the Second Polynomial, enter the details of the", n2,"terms below:")
for i in range(n2):
    print("\nEnter the details of Term # ", i+1,": ", sep='')
    poly2[i][0]= int(input("Enter the magnitude: "))
    poly2[i][1]= int(input("Enter the coefficient: "))

print("\nThe sum of the two polynomials:\n", polytoexpn(sumOfPolynomials(poly1, poly2)),
    "\n\nThe difference of the two polynomials: ", polytoexpn(diffOfPolynomials(poly1, poly2)))

'''
This program has two phases: Only if you do the phase 1 correctly that you can even think of
trying the second phase.

PHASE 0:
Design a proper function structure for this program. Indispensable for any constructive work.

PHASE 1:
Extract the magnitude and coefficients of the polynomial from each of the given expressions.
Here you need to handle certain string related difficulties like handling intervening spaces,
special characters etc. Infact the MOST DIFFICULT part.

PHASE 2:
As and when the magnitudes and coefficients have been SUCCESSFULLY EXTRACTED, that you plan
the summation and difference operations with the given polynomials.
'''

'''               
    The above extraction of values and coefficients need to be done using only a SINGLE LOOP...  
    but with PROPER PLANNING...

    Say:
    You start traversing...extracting each character... if its a digit you do something... 
    On encountering a non-digital character check if its x or ^ x ignore, ^ then the new (few) digits(s)
    should be treated properly as power.
    This way the extraction will go onclick
    Sir will the extraction happen in 2 single d arrays or one 2d array?
    ONE 2-D Cross-linked!!  And you have done that topic at my place. yes

    Almost like word extraction algorithm, this extraction shall also have block-codes doing 
    specific operations... primarily of storage only...
    This is the MOST IMPORTANT STEP.

    You should once print the extracted entities on screen to verify if the extraction has been done CORRECTLY
    or not.
    If done, THEN ONLY proceed to the simpler operation of poly add and sub...
    Even after addition and sub... the formation of the poly expression is pretty simple...
    Only the EXTRACTION PART is difficult.
'''