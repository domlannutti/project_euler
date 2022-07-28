## Problem statement
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

## Solution
def is_palindrome(num: int) -> bool:
    if str(num) == str(num)[::-1]:
        return True
    return False

def main() -> int:
    pal = []
    for i in range(100, 1000):
        for j in range(100, i):
            if is_palindrome(i*j):
                pal.append(i*j)
    return max(pal) 

if __name__ == "__main__":
    print(main())
