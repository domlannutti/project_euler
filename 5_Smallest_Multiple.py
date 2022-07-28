## Problem statement
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Solution
def sieve_of_eratosthenes(lim: int) -> int:
    prime = [True] * lim
    prime[0], prime[1] = False, False
    
    for i in range(len(prime)):
        if prime[i] == True:
            yield i
            
            j = 2
            while i*j < len(prime):
                prime[i*j] = False
                j += 1

def prime_factorization(n: int, primes: list) -> dict:
    factors = dict()
    for p in primes:
        while n % p == 0:
            if p not in factors:
                factors[p] = 1
            else:
                factors[p] += 1
            n //= p
        if p > n:
            return factors

def smallest_mult(lim: int) -> int:
    if lim < 0:
        return 0
    elif lim < 2:
        return lim
    
    res_factors = dict()
    res = 1
    primes = [x for x in sieve_of_eratosthenes(lim+1)]

    for i in range(2, lim+1):
        for key, value in prime_factorization(i, primes).items():
            if key not in res_factors:
                res_factors[key] = value
            elif value > res_factors[key]:
                res_factors[key] = value
    
    for key, value in res_factors.items():
        res = res*key**value
    return res


if __name__ == "__main__":
    print(smallest_mult(20))
