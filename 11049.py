import sys
n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*(n) for _ in range(n)]

for mid in range(1, n):
    for start in range(n):  
        if start + mid == n: 
            break
        #만약에 s+m이 n과 같아진다면 끝점이기 때문

        dp[start][start+mid] = int(1e9)
        
        for t in range(start, start+mid):
            dp[start][start+mid] = min(dp[start][start+mid],
                                        dp[start][t]+dp[t+1][start+mid] + arr[start][0] * arr[t][1] * arr[start+mid][1])

print(dp[0][n-1])