number=int(input("Enter a number: "))
sum=0
for i in range(1,number+1):
    if i%2==0:
        sum+=i
print(f"The sum of all even number between 1 and {number} is: {sum}")
