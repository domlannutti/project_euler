## Problem statement
# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 3025
# Hence the difference between the sum of the squares of the first natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

## Solution
def sum_of_squares(n: int) -> int:
    res = 0
    for i in range(1, n+1):
        res += i**2
    return res

def square_of_sums(n: int) -> int:
    return sum([x for x in range(1, n+1)])**2

def main(n: int) -> int:
    if n < 0:
        return None
    elif n % 1 != 0:
        return None
    
    return square_of_sums(n) - sum_of_squares(n)

if __name__ == "__main__":
    print(main(100))
