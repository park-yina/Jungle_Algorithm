import sys
import heapq

INF = 987654321
input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def daik(s):
    q = []
    distance[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for next_node in graph[cur]:
            cost = dist + next_node[1]
            if distance[next_node[0]] > cost:
                distance[next_node[0]] = cost
                heapq.heappush(q, (cost, next_node[0]))

daik(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])