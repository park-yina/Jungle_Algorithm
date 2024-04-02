from collections import deque
n,m= map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))
def bfs(x,y):
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(len(dx)):
            nx=x+dx[i]
            ny=y+dy[i]
            if(nx>=n or ny>=m or nx<0 or ny<0):
                continue
            if(graph[nx][ny]==0):
                continue
            if(graph[nx][ny]==1):
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))