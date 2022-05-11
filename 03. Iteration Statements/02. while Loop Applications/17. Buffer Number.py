import os
os.system("cls")

print("To check if a given number is a Buffer number or not:")
first2digs = num = int(input("Enter an integer: "))

last2digs = num%100
while(first2digs > 100):
    first2digs//= 10
sum_first = first2digs//10 + first2digs%10
sum_last = last2digs//10 + last2digs%10

print("\nThe integer ",num," is ",
    "" if(sum_first==sum_last) else "NOT ", 
    "a Buffer number\n", sep='')
