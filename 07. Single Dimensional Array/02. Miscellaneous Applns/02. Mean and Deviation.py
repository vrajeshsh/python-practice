import os
os.system("cls")

print("To calculate mean of all heights and display it's deviation:\n")
n = int(input("Enter number of heights: "))
print()

ssum, hgt, dev, max_dev, max_pos = 0, [], "", 0, 0
for i in range(n):
    print("Enter height #", i+1,": ", sep='', end='')
    hgt.append(float(input()))
    ssum+=hgt[i]

mean = round(ssum/n,3)
print("\nMean of all heights: ",mean)
print("\nHEIGHT\t\tDEVIATION FROM MEAN\n")
for i in range(len(hgt)):
    dev = round(abs(mean-hgt[i]),3)
    print(hgt[i],"\t\t",dev)
    if dev>max_dev:
        max_dev = dev
        max_pos = i

print("\nPosition of the element with the highest deviation:",max_pos+1,"\n")