number=int(input("Enter a number: "))
div=[]
for i in range(1,number+1):
    if number%i==0:
        div.append(i)

print("The divisors of",number,"are",div)
