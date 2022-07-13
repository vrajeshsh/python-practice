import os
os.system("cls")

final_cnt, i = 0, 0
print("To calculate minimum notes required to generate amount:\n")
amt = int(input("Enter amount: Rs "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
print("\nThe generated currency notes for Rs",amt,"are as follows:\n")
while amt > 0:
    count = amt//notes[i]
    if count > 0:
        final_cnt+=count
        print("Rs "+str(notes[i])+" x "+str(count)+" = "+str(notes[i]*count))
        amt%= notes[i]
    i+= 1
   
print("\nNumber of currency notes generated:", final_cnt,"\n")
