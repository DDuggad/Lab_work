import os
filename = input("Enter filename: ").strip()
if '.txt' not in filename:
    filename=filename+'.txt'

try:
    txt = open(filename)
except:
    print("File can't be opened.")
    exit()
count={"lines":0,"words":0,"char":0}
for line in txt:
    count["lines"]+=1
    words = line.split()
    for word in words:
        count["words"]+=1
        for char in word:
            count["char"]+=1

print("The count is: ",count)
        
