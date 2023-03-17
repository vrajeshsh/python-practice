import os
os.system('cls')

class LargeNum():
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

    def scalarProduct(self, n):
        prod, carry = "", 0
        for dig in self.num[::-1]:
            digProd = (ord(dig)-48)*n+carry
            carry = digProd//10
            prod= chr(digProd%10+48)+prod
        if carry>0:
            prod= chr(carry+48)+prod
        return prod

    def getSum(self, num):
        sum, carry, i, j  = "", 0, len(self.num)-1, len(num.num)-1
        while i>=0 or j>=0:
            dig1, dig2 = self.num[i] if i>=0 else "0", num.num[j] if j>=0 else "0"
            digSum = ord(dig1)-48 + ord(dig2)-48 + carry
            carry = digSum//10
            sum= chr(digSum%10+48)+sum
            i-=1
            j-=1
        if carry>0:
            sum= chr(carry+48)+sum
        return LargeNum(sum)
    ''' The below method code is NOT PROPERLY DEFINED. You need to work on it. First make it happen
    'ANY WAY' After it starts yielding correct output, sit to TUNE THE CODE. '''
    def multiply(self, num1, num2):
        sum, pow = 0, 0
        for dig in num2.num[::-1]:
            prod = self.scalarProduct(num1, dig)
            print(prod)
        print(sum)

print("To display the product of two large numbers:")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

obj1, obj2, prod = LargeNum(num1), LargeNum(num2), LargeNum("0")
print("\nFirst Number: ", sep='', end='')
obj1.display()
print("Second Number: ", sep='', end='')
obj2.display()
for i in range(10, 15):
    print(num1," x ", i, " = ", obj1.scalarProduct(i), sep='')
# print("\nTheir Product: ", sep='', end='')
# prod.multiply(obj1, obj2)
# prod.display()

'''
Sum and Scalar product (the most important method in this class) working... 
You should now have no difficulty in FIXING and Finalizing the multiplication method.

Work, if you like...
Will check the program and Fix if necessary TOMORROW in class.  
'''