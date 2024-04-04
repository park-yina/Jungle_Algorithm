import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
queue = deque()
result = []
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    degree[b]+=1
for i in range(1,n+1):
    if(degree[i]==0):
        queue.append(i)
while queue:
    cur=queue.popleft()
    result.append(cur)
    for i in graph[cur]:
        degree[i] -= 1
        if(degree[i]==0):
            queue.append(i)
print(*result)