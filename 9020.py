import math
import sys

def is_prime(n):
    if n == 1:
        return False
    k = int(math.sqrt(n))
    for i in range(2, k + 1):
        if n % i == 0:
            return False
    return True
