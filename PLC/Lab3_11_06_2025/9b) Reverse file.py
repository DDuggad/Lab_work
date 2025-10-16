import os
import string
filename = input("Enter filename: ").strip()
if '.txt' not in filename:
    filename=filename+'.txt'

try:
    file = open(filename, 'r')
    txt = file.read()
except:
    print("File can't be opened.")
    exit()
 
lines = txt.splitlines()
reversed_lines = lines[::-1]
reversed_content = "\n".join(reversed_lines)

print(f"\nReversed Content (line by line):\n \n{reversed_content.strip()}\n")

print(f"\nReversed Content (word by word):\n")

for line in lines:
    words=line.split()
    words=words[::-1]
    for word in words:
        cleaned_word = ""
        for char in word:
            if char not in string.punctuation:
                cleaned_word += char
        print(cleaned_word, end=" ") 
    print() 

print("\n")
   
