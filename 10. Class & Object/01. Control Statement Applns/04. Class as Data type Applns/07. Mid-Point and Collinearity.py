import os
os.system("cls")

class Point():

    def readPoint(self):
        self.x = int(input("Enter x-coordinate: "))
        self.y = int(input("Enter y-coordinate: "))

    def showPoint(self):
        print("(",self.x,", ",self.y,")", sep='')

    def distance(self, pt):
        return ((self.x - pt.x)**2+(self.y - pt.y)**2)**0.5

    def midPoint(self, pt):
        midPt = Point()
        midPt.x= (self.x + pt.x)/2
        midPt.y= (self.y + pt.y)/2
        return midPt

    def area(self, pt1, pt2):
        a, b, c = self.distance(pt1), self.distance(pt2), pt1.distance(pt2)
        s = (a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c))**0.5

    def isCollinear(self, pt1, pt2):
        return self.area(pt1, pt2)==0

pt1, pt2, pt3 = Point(), Point(), Point()                       # --> D
                                                                # --> I    
print("To find the mid-points and check the collinearity for three points: ")
print("\nEnter the coordinates of the First point:")
pt1.readPoint() 
print("Enter the coordinates of the Second point:")
pt2.readPoint()
print("Enter the coordinates of the Third point:")
pt3.readPoint()
                                                                # --> P
midpt1, midpt2, midpt3 = pt1.midPoint(pt2), pt2.midPoint(pt3), pt1.midPoint(pt3)
area= pt1.area(pt2, pt3)
                                                                # --> O
print("\nThe points given are as follows:",
    "\nFirst point: ")
pt1.showPoint()
print("Second point: ")
pt2.showPoint()
print("Third point: ")
pt3.showPoint()
print("\nThe mid-pont of the points are as follows:",
"\nMid-point of First and Second points:")
midpt1.showPoint()
print("Mid-point of Second and Third points:")
midpt2.showPoint()
print("Mid-point of First and Third points:")
midpt3.showPoint()
if pt1.isCollinear(pt2, pt3):
    print("\nThe three points are Collinear!\n")
else:
    print("\nThe three points are non-collinear.",
        "\nThe area of the triangle contained by the points: ",round(area, 3), " sq units\n", sep='')