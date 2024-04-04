import sys


input_a = sys.stdin.readline().rstrip()

input_b = sys.stdin.readline().rstrip()

len_a = len(input_a)
len_b = len(input_b)

dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]

# LCS 길이 계산
for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        if input_a[i - 1] == input_b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
