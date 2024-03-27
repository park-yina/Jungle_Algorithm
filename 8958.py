import sys

n = int(sys.stdin.readline())

for _ in range(n):
    arr = input()
    res = 0
    continuity = 0

    for j in arr:
        if j == 'O':
            continuity += 1
        else:
            continuity = 0
        res += continuity

    print(res)
