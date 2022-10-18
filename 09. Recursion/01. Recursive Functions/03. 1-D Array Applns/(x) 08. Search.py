import os
os.system("cls")

#Below function is NOT WORKING. Kindly fix the code whenever free
def search(arr, srchelem): 
    global j
    j+=1
    if j==len(arr)-1:
        return -1
    if arr[j]==srchelem:
        return j
    search(arr, srchelem)

j = -1
print("To search an element within an array:")
n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    print("Enter element #",(i+1),": ", sep='', end='')
    arr.append(int(input()))

srchelem = int(input("\nEnter the element to search: "))

print("\nThe array:\n",arr,sep='')

srchpos = search(arr, srchelem)+1

if srchpos is not None:
    print("\n",srchelem," is present at position: ",srchpos,"\n",sep='', end='')
else:
    print("\n",srchelem," is NOT present in the array!\n",sep='')


