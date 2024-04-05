import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m + 1)
    dp[0] = 1


    for j in coin:
        for i in range(m + 1):
            if i >= j:
                dp[i] += dp[i - j]
                #만들 수 있는 경우와 없는 경우를 분리하여 이전경우의 수+ 현재 경우의수
    print(dp[m])