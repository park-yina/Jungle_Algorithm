import collections
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(input().strip()) for _ in range(r)]
dist = [[0] *c for _ in range(r)]
dx= [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = collections.deque()

def bfs(s,e):
    while queue:
        x,y = queue.popleft()
        if graph[s][e] == 'S':
            return dist[s][e]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx,ny))
                elif (graph[nx][ny] =='.' or graph[nx][ny] =='S') and graph[x][y] == '*':
                    #고슴도치처럼 물도 이동처리 해주어야한다.
                    graph[nx][ny] = '*'
                    queue.append((nx,ny))
    return "KAKTUS"


for x in range(r):
    for y in range(c):
        if graph[x][y] == 'S':
            queue.append((x,y))
        elif graph[x][y] == 'D':
            Dx,Dy = x,y

for x in range(r):
    for y in range(c):
        if graph[x][y] == '*':
            queue.append((x,y))

print(bfs(Dx,Dy))
