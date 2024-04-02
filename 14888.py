import sys
from collections import deque
input = sys.stdin.readline
n=int(input())
num = list(map(int, input().split()))
operator= list(map(int, input().split()))
max_num=-1e8
min_num=1e8
def dfs(cnt,total,plus,minus,mul,div):
    global max_num,min_num
    if(cnt==n):
        max_num=max(max_num,total)
        min_num=min(min_num,total)
        return
    if plus:
        dfs(cnt+1,total+num[cnt],plus-1,minus,mul,div)#탐색을 할 때마다 cnt를 올려주고 대신 연산자를 빼주고 나머지 연산자는 냅둔다
    if minus:
        dfs(cnt+1,total-num[cnt],plus,minus-1,mul,div)
    if mul:
        dfs(cnt+1,total*num[cnt],plus,minus,mul-1,div)
    if div:
        dfs(cnt+1,total/num[cnt],plus,minus,mul,div-1)
dfs(1,num[0],operator[0],operator[1],operator[2],operator[3])
print(max_num)
print(min_num)
