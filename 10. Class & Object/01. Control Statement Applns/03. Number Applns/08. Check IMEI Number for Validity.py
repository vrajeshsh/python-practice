# I AM CODING IN 2022 FOR US JOBS!! 

import os
os.system("cls")

class IMEINumber():
    def __init__(self, num):
        self.imeiNum = num

    def digitSum(self, n):
        ssum = 0
        while n>0:
            ssum+= n%10
            n//=10
        return ssum

    def isValid(self):
        temp, count, ssum = self.imeiNum, 0, 0
        while temp>0:
            dig = temp%10
            ssum+= dig if count%2==0 else self.digitSum(dig*2)
            count+=1
            temp//=10
        return ssum%10==0

print("To check whether or not the IMEI Number is valid:")
num = int(input("Enter the IMEI Number: "))

obj = IMEINumber(num)        
print("\nThe IMEI Number is ", "" if obj.isValid() else "in",
    "valid!\n", sep='')

            