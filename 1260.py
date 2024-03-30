from collections import deque

n, m, v = map(int, input().split())
graph = [[False] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

def bfs(s):
    queue = deque([s])
    visited = [False] * (n+1)
    visited[s] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if not visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True

dfs(v)
print()
bfs(v)
