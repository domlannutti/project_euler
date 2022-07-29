## Problem statement
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

## Solution
def sieve_of_eratosthenes(lim: int) -> int:
    primes = [True] * lim
    primes[0], primes[1] = 0, 0

    for p in range(len(primes)):
        if primes[p] == True:
            yield p

            i = 2
            while p*i < lim:
                primes[i*p] = False
                i += 1

def prime_summation(target: int) -> int:
    summation = 0
    for p in sieve_of_eratosthenes(target):
        summation += p
    return summation


if __name__ == "__main__":
    print(prime_summation(2*10**6))
