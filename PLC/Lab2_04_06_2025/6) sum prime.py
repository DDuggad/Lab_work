sum_of_primes=0
for num in range(2,2000000):
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        sum_of_primes +=num

print("Sum of all primes below two million: ",sum_of_primes)
