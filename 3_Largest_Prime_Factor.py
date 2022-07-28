## Problem statement
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Solution
def sieve_of_eratosthenes(lim: int) -> int:
    prime = [True]*lim
    prime[0] = False
    prime[1] = False

    for i in range(len(prime)):
        if prime[i] == True:
            yield i
            for j in range(2, len(prime)//i):
                prime[i*j] = False

def main(lim: int) -> int:
    primes = [x for x in sieve_of_eratosthenes(int(lim**0.5))]
    for i in primes[::-1]:
        if lim % i == 0:
            return i    
    return lim

if __name__ == "__main__":
    print(main(600851475143))
