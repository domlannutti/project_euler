## Problem statement

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

## Solution

def multsum(lim: int, multiples: list) -> int:
    res = 0
    for i in range(lim):
        for n in multiples:
            if i % n == 0:
                res += i
                break
    return res

if __name__ == "__main__":
    multsum(1000, [3, 5])
