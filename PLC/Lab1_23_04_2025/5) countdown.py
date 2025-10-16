import time
while True:
    number=int(input("Enter a number: "))
    if number>0:
        break
    else:
        print("Enter a valid positive integer.")
count=number
while count>=0:
    print(count)
    time.sleep(2)
    count-=1
