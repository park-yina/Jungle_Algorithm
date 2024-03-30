from collections import deque

def dfs(graph, s, visit):
    stack = [s]
    while stack:
        node = stack.pop()
        if not visit[node]:
            visit[node] = True
            for next in reversed(graph[node]):
                if not visit[next]:
                    stack.append(next)

# 그래프 정보 입력
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 방문 여부를 체크할 리스트
visit = [False] * (n+1)

# 연결 요소 개수 세기
count = 0
for i in range(1, n+1):
    if not visit[i]:
        dfs(graph, i, visit)
        count += 1

# 결과 출력
print(count)
