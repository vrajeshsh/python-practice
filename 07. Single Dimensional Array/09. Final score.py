import os
os.system("cls")

print("To calculate score by removing highest and lowest and averaging the other values:\n")

scores, ssum = [], 0
print("Enter score between 0 and 10 only:")
for i in range(10):
    print("Enter score #", i+1,": ", sep='', end='')
    scores.append(float(input()))
    if 0<=scores[i]<=10:
        ssum+=scores[i]
    else:
        print("\nKindly enter score between 0 - 10!\n")
        exit()

final = round((ssum-max(scores)-min(scores))/8,3)
scores.remove(max(scores))
scores.remove(min(scores))

#Kindly make provision to display the 'permissible scores' of the candidate
print("\nScores:\n",scores,
    "\n\nThe final score of the candidate: ",final,"\n", sep='')

# Fix this for tomorrow. Will see it in class. 