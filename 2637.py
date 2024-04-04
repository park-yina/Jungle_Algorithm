import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
needs = [[0] * (n + 1) for _ in range(n + 1)]  # 각 제품을 만들때 필요한 부품
q = deque()
degree = [0] * (n + 1)
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))
    degree[a] += 1

for i in range(1, n + 1):
    # 위상정렬 위해 우선 0인거 죄다 넣음
    if degree[i] == 0:
        q.append(i)
while q:
    cur = q.popleft()
    for next, next_needs in graph[cur]:
        if all(needs[cur][k] == 0 for k in range(n + 1)):
            # 카운트가 0이고 n+1이라는 것은 기본 부품이니까 그냥 가중치만큼만
            needs[next][cur] += next_needs
        else:
            for k in range(1, n + 1):
                needs[next][k] += needs[cur][k] * next_needs
                # 중간 부품이라면 필요 숫자만큼 곱
        degree[next] -= 1
        if degree[next] == 0:
            # 차수 0이면 큐에 넣음
            q.append(next)

for x in enumerate(needs[n]):
    if x[1] > 0:
        print(*x)