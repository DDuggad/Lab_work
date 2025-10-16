def sieve_of_eratosthenes(n):
    # Initialize a list of truth values for numbers 0 to n-1 (all assumed prime initially)
    sieve = [True] * n  
    sieve[0:2] = [False, False]  # 0 and 1 are not prime numbers

    # Loop only up to the square root of n for efficiency
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            # Mark multiples of i starting from i*i as non-prime
            for j in range(i * i, n, i):
                sieve[j] = False
    return sieve

# Get the upper limit from the user:
range1 = int(input("Enter a number: "))

# Create the sieve and generate the list of primes below range1:
sieve = sieve_of_eratosthenes(range1)
prime_sum = sum(i for i, is_prime in enumerate(sieve) if is_prime)

print(f"The sum of all prime numbers below {range1} is: {prime_sum}")

# Get the upper limit from the user:
range1 = int(input("Enter a number: "))

# Create a list to represent if numbers are prime (True means assumed prime)
sieve = [True] * range1

# 0 and 1 are not prime numbers
if range1 > 0:
    sieve[0] = False
if range1 > 1:
    sieve[1] = False

# Use the Sieve algorithm to mark non-prime numbers:
# Only need to check up to the square root of range1.
for i in range(2, int(range1 ** 0.5) + 1):
    if sieve[i]:
        # Mark multiples of i starting from i*i as non-prime
        for j in range(i * i, range1, i):
            sieve[j] = False

# Sum up all the numbers that remain marked as True (primes)
prime_sum = 0
for idx, is_prime in enumerate(sieve):
    if is_prime:
        prime_sum += idx

print("The sum of all prime numbers below", range1, "is:", prime_sum)
