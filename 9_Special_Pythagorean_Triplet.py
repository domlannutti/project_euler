## Problem statement
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

## Solution
def triplet(target: int) -> int:
    for m in range(3, target, 2):
        for n in range(1, m, 2):
            a = m * n
            b = (m**2 - n**2) // 2
            c = (m**2 + n**2) // 2
            if a+b+c == target:
                return a*b*c
    return 0


if __name__ == "__main__":
    print(triplet(1000))
