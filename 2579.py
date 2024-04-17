import sys
input=sys.stdin.readline
n=int(input())
step = [int(input()) for _ in range(n)]
arr=[]
dp=[0]*n#0*n으로 초기화 해주어야 점화식에서는 오류가 나지 않음
#점화식은 n이 1또는 2일때는 그냥 하고, 3에서는 연속된 두개를 밟을 것인지 정해야한다.
dp[0]=step[0]
if n>1:
    dp[1]=dp[0]+step[1]
for i in range(2,n):
    dp[i]=max(dp[i - 2] + step[i], dp[i - 3] + step[i - 1] + step[i])
print(dp[-1])