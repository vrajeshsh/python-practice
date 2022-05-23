import os
os.system("cls")

def celToFah(cent):
    return 1.8*cent+32

print("\nTo convert centigrade to fahrenheit in a given range:")
start = int(input("Enter start limit: "))
end = int(input("Enter end limit: "))

print("\nCentigrade\tFahrenheit")
for i in range(start, end+1):
    print(i, "\t\t", round(celToFah(i), 2))
print()
