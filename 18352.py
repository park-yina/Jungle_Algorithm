from collections import deque
n,m,k,x=map(int,input().split())
graph=[[]for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
dist=[-1]*(n+1)
dist[x]=0
queue=deque()
queue.append(x)
while queue:
    node=queue.popleft()
    for next in graph[node]:
        if(dist[next]==-1):
            dist[next]=dist[node]+1
            queue.append(next)
visit=False
for i in range(1,n+1):
    if(dist[i]==k):
        print(i)
        visit=True
if visit==False:
    print(-1)
