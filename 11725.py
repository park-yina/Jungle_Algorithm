import sys
from collections import deque
input = sys.stdin.readline
n=int(input())
graph = [[0] for _ in range(n+1)]
parent=[0]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
parent[1]=0
q=deque()
q.append(1)
while q:
    cur=q.popleft()
    for i in graph[cur]:
        if(parent[i]==0):
            parent[i]==cur
            q.append(i)
print('\n'.join(map(str, parent[2:])))
