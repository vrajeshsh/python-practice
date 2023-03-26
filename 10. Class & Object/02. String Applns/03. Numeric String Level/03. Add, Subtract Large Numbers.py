import os
os.system('cls')

class BigNum():
    def __init__(self, n):
        self.num = ""
        if not n.isdigit():
            print("\nInvalid number entered!\n", sep='')
            exit()
        else:
            for dig in n:
                if not (self.num=="" and dig=="0"):
                    self.num+= dig

    def display(self):
        print(self.num, sep='')

    def check(self, num):
        return 0 if self.num == num.num else 1 if self.num > num.num else -1     

    def sum(self, num):
        ''' Follow the below given algorithm to complete/improve the below code:
        1. Run an inter-locked loop to traverse both the numbers from the rear-end.
        2. Extract the digits from the two numbers (only if the length allows, otherwise use a 0).
        3. Get the sum(s) by adding the two digits alng with the carry.
        4. Finalize and set the sum and carry if the s > 10.
        5. Keep catenating reversely in the string sum, converting the 's' to string intermediately.
        All these should take about 3 lines only.
        6. Now outside the loop, check for dangling carry. This occurs when you have a carry even after
           the loop ends. If its exists then shove that too in the sum string catenating reversely.
        7. Finally put the string in an object of the given class and return it.
        '''

        sum, carry, i, j  = "", 0, len(self.num)-1, len(num.num)-1
        while i>=0 or j>=0:     # running the loop till the greater number
            dig1, dig2 = self.num[i] if i>=0 else "0", num.num[j] if j>=0 else "0"
            digSum = ord(dig1)-48 + ord(dig2)-48 + carry
            carry = digSum//10
            sum= chr(digSum%10+48)+sum
            i-=1
            j-=1
        if carry>0:
            sum= chr(carry+48)+sum
        return BigNum(sum)

    def subtract(self, num1, num2):
        diff, borrow, i, j = "", 0, len(num1)-1, len(num2)-1
        while i>=0 or j>=0:
            dig1, dig2 = num1[i] if i>=0 else "0", num2[j] if j>=0 else "0"
            digDiff = (ord(dig1)-48) - (ord(dig2)-48) - borrow
            if digDiff<0:
                digDiff+= 10
                borrow = 1
            else:
                borrow = 0
            diff=chr(digDiff+48)+diff
            i-=1
            j-=1
        return BigNum(str(int(diff)))

print("To display the bigger of two big numbers and also find their sum and difference:")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

obj1, obj2, diff = BigNum(num1), BigNum(num2), BigNum("0")
sum = obj1.sum(obj2)

print("\nFirst Number: ", sep='', end='')
obj1.display()
print("Second Number: ", sep='', end='')
obj2.display()
chkVal = obj1.check(obj2)
if chkVal > 0:
    print("\nThe first number is larger.")
elif chkVal < 0:
    print("\nThe second number is larger.")
else:
    print("\nThe numbers are equal!")
print("\nSum of the two numbers:")
sum.display()
print("\nAbsolute difference:")
diff.subtract(num1, num2).display()
print()