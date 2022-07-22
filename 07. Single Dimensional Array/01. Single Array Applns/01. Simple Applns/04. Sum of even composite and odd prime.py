import os
os.system("cls")

def isPrime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

nums, odd_primes, odd_sum, even_comps, even_sum = [], "", 0, "", 0
print("To display the sum of even composite and odd prime numbers:")
n = int(input("Enter number of elements: "))
print()

for i in range(n):
    print("Enter element #", i+1,": ", sep='', end='')
    nums.append(int(input()))

for num in nums:
    if isPrime(num):
        if num>2:
            odd_primes+= str(num) if odd_primes== "" else ", "+str(num)
            odd_sum+= num
    elif num>3 and num%2==0:
        even_comps+= str(num) if even_comps== "" else ", "+str(num)
        even_sum+= num

print("\nThe array:\n", nums, "\n", sep='')
if even_sum==0:
    print("\nNo even-Composite numbers exist in the array!\n")
else:
    print("\nThe even composite numbers are:\n", even_comps,
        "\nSum of the even composite numbers: ", even_sum)
if odd_sum==0:
    print("\nNo odd-Prime numbers exist in the array!\n")
else:
    print("\nThe odd Prime numbers are:\n", odd_primes,
        "\nSum of the odd prime numbers: ", odd_sum, "\n")

# Are you purtubbed for any reason that you are NOT READING program descriptions these days?
'''Now answer: sorry sir am just too tired today.. no Excuse but wont happen again'''
