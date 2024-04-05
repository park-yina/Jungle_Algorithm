n = int(input())
arr = list(map(int, input().split()))

dp = [0] * (n)
dp[0] = 1

if n == 1:
    print(1)
    exit()

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1

print(max(dp))
