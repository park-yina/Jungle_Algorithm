import sys

def input():
    global a, b, c
    a, b, c = map(int, sys.stdin.readline().split())

def power(x, y, m): 
    if y == 0:
        return 1
    p = power(x, y // 2, m) % m
    p = (p * p) % m
    return (p if y % 2 == 0 else (x * p) % m)

def solve():
    input()  # input 함수 호출
    res = power(a, b, c)
    print(res)

solve()
