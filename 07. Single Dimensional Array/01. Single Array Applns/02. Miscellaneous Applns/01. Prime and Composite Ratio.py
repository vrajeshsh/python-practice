import os
os.system("cls")

def isprime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print("To calculate the ratio of justprime to composite:\n")
n = int(input("Enter number of elements: "))
print()

nums, prime_cnt, comp_cnt = [], 0, 0
for i in range(n):
    print("Enter element #", i+1,": ", sep='', end='')
    nums.append(int(input()))
    if isprime(nums[i]):
        prime_cnt+=1
        print(nums[i],"Prime")
    elif nums[i]>3:
        print(nums[i],"Composite")
        comp_cnt+=1
      
i = 2
while i<prime_cnt and i<comp_cnt:
    if prime_cnt%i==0 and comp_cnt%i==0:
        prime_cnt//=i
        comp_cnt//=i
        i-=1
    i+=1
print("\nRatio of Prime : Composite = ",prime_cnt," : ",
        comp_cnt,"\n", sep="")
