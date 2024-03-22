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

cnt = 0
num = int(input())
for _ in range(num):
    input_values = list(map(int, sys.stdin.readline().split()))
    for val in input_values:
        if is_prime(val):
            cnt += 1

print(cnt)
