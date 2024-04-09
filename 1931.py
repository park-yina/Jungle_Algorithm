import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    temp = [list(map(int, input().split())) for _ in range(n)]
    arr = sorted(temp)
    top = 0
    res = 1
    
    for i in range(1, len(arr)):
        if arr[i][1] < arr[top][1]:
            top = i
            res += 1
    
    print(res)