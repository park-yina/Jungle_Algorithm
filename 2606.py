import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visit = [[False] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0

def bfs(start):
    q = deque([start])
    visit[start][0] = True  
    global cnt

    while q:
        i = q.popleft()  
        for j in graph[i]:
            if not visit[j][0]:  # 이미 방문한 정점이 아닌 경우에만 실행
                #이거 안해줘서 아까 틀렸음...멍청비용
                visit[j][0] = True
                cnt += 1
                q.append(j)

bfs(1)
print(cnt)
