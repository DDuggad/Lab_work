while True:
    count = int(input("Enter no. of Fibonacci numbers to be generated: "))
    if count <=0:
        print (f"Enter a valid positive integer, not {count}.")
    else:
        break
fib_sequence=[]
a,b=0,1
for i in range(count):
    fib_sequence.append(a)
    a,b=b,a+b
print("Fibonacci sequence: ", fib_sequence)
