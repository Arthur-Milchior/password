import os
import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"
def permut(mot,first_letter_pos):
    return mot[first_letter_pos:]+mot[:first_letter_pos]

successor = {l:ll for (l,ll) in zip(alphabet, permut(alphabet,1))}

mots=[]
with open("pwd_parameter") as f:
    lines=f.read().splitlines()
    for i in range(6):
        mots.append(lines[i])
    numbers = lines[6]
letters= sys.argv[1]


concat= ""
for mot in mots:
    concat=concat+mot
length = len(concat)

def find(letter, concat):
    while True:
        for (i,l) in enumerate(concat):
            if l == letter:
                return i
        letter = successor[letter]

answer=""
for letter,number in zip(letters,numbers):
    pos = find(letter,concat)+int(number)
    answer+=concat[pos:pos+3]
    concat=permut(concat,pos)

print(answer)
