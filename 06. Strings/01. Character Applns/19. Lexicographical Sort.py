from email.errors import InvalidBase64CharactersDefect
import os
os.system("cls")

def stringSort(str):
    sorted_str =""
    
    for ascii in range(0, 91):
        char = chr(ascii)
        for ch in str:
            # Anchoring the symbols after the digits and to tackle only once below
            if char=='9' and not ch.isalnum() and ch!= ' ':
                sorted_str+= ch
            if char == ch.upper():
                sorted_str+= ch
    return sorted_str

str = input("Enter a string to sort lexicographically:\n")

print("\nLexicographically (dictionary) sorted string:\n",
    stringSort(str),"\n", sep='')

'''
You may follow this algorithm:
1. Set an outer loop to generate the ASCII values from the lowest to
   highest as applicable.
2. Within this loop set a loop to extract the characters of the string
   to be sorted.
3. As and when the ASCII value of the character extracted matches that
   of the outer loop ASCII value, build a new string.
   Primary arrangement of the characters will be done by this. What
   would remain is keeping the symbols anchored at the left side after
   the digits.
4. To fix the symbols stay anchored in between the digits and letters,
   just keep a check to ensure manually that the symbols enter the new 
   sorted string after the digits only.
That's it. Just print that new sorted string.   
'''
