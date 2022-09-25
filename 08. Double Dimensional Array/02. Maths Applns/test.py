from logging.config import valid_ident
import os
os.system("cls")

def expntopoly(polyexpn):
    temp = [0, 0]
    res = []
    for i in polyexpn:
        if i in "+-":
            temp[1]=val
            res.append(temp)
            val = ""
        elif i=="x":
            temp[0]=val

        elif i == " " or i in "^":
            continue
        else:
            val.append(i)

polyexpn = "2x^45 - 12x^566 + 49x^78"

print(expntopoly(polyexpn))

