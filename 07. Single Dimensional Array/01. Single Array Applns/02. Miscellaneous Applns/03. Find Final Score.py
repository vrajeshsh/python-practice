import os
os.system("cls")

scores, permi_scores, ssum = [], [], 0

print("To calculate score by removing highest and lowest and averaging the other values:\n")
print("Enter score between 0 and 10 only:")
for i in range(10):
    print("Enter score #", i+1,": ", sep='', end='')
    scores.append(float(input()))
    permi_scores[i]= scores[i]
    if 0<=scores[i]<=10:
        ssum+=scores[i]
    else:
        print("\nKindly enter score between 0 - 10!\n")
        exit()

final = round((ssum-max(scores)-min(scores))/8,3)
permi_scores.remove(max(scores))
permi_scores.remove(min(scores))

print("\nThe original scores obtained by the Diver:\n",scores,
    "\nThe permissible scores of the Diver:\n", permi_scores,
    "\n\nThe final score of the candidate: ",final,"\n", sep='')

# To get a few special scores, you ran 4 loop-invoking functions!!
# At a highesr level you will learn how to find it frugally in that
# one input loop only...