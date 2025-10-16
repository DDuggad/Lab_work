filename = input("Enter filename: ").strip()
if '.txt' not in filename:
    filename=filename+'.txt'

try:
    txt = open(filename)
except:
    print("File can't be opened.")
    exit()
count=dict()
for line in txt:
    words = line.split()
    for word in words:
        if word not in count:
            count[word]=1
        else:
            count[word]+=1
    
print("The Frequency is: ",count)
