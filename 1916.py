import sys
import heapq

INF = 987654321
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

start, end = map(int, input().split())

def daik(s, n):
    distance = [INF] * (n + 1)
    distance[s] = 0
    heap = []
    heapq.heappush(heap, [0, s])
    
    while heap:
        cur_cost, cur_v = heapq.heappop(heap)
        if distance[cur_v] < cur_cost:
            continue
        for next_v, next_cost in graph[cur_v]:
            sum_cost = cur_cost + next_cost
            if sum_cost >= distance[next_v]:
                continue
            
            distance[next_v] = sum_cost
            heapq.heappush(heap, [sum_cost, next_v])
    
    return distance

result = daik(start, n)
print(result[end])
