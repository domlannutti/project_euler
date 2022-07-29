## Problem statement
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

## Solution
def sieve_of_eratosthenes(lim: int) -> int:
    primes = [True] * lim
    primes[0], primes[1] = False, False

    for i in range(len(primes)):
        if primes[i] == True:
            yield i

            j = 2
            while i*j < len(primes):
                primes[i*j] = False
                j += 1


def prime_counter(n: int) -> int:
    count = 0
    for i in sieve_of_eratosthenes(10**6):
        count += 1
        
        if count == n:
            return i

    print("Sieve of Eratosthenes limit set too low to capture prime number at index {}".format(n))


if __name__ == "__main__":
    print(prime_counter(10001))
