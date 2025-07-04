# Create a set of prime numbers less than 50
primes = set()
for num in range(2, 50):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.add(num)
n = int(input("Enter a number to check: "))
if n in primes:
    print(f"{n} is a prime number less than 50.")
else:
    print(f"{n} is not a prime number less than 50.")

