import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def bfs(x):
    visit[x]=1
    q = deque()
    q.append(x)
    while q:
        next = q.popleft()
        for i in que[next]:
            if visit[i]==0:
                visit[i] = -1*visit[next]
                q.append(i)
            else:
                if visit[i] == visit[next]:
                    return False
    return True


k = int(input())
for i in range(k):
    v, e = map(int, input().split())
    que = [[] for i in range(v+1)]
    visit = [0]*(v+1)
    flg = 1
    for j in range(e):
        a, b = map(int, input().split())
        que[a].append(b)
        que[b].append(a)
    for k in range(1, v+1):
        if visit[k]==0:
            if not bfs(k):
                flg = -1
                break
    print('YES' if flg==1 else 'NO')