import sys
import heapq
INF=987654321
input=sys.stdin.readline
n,m=map(int,input().split)
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
def daik(s):
  q=[]
  distance[s]=0
  heapq.heappush(q,(0,s))# 이렇게 해서 빈 큐에는 우선순위를 넣고 나머지에는 s에 대한 거리를 관리한다
  while q:
    dist,cur=heapq.heappush(q)
    if(distance[cur]<dist):
      continue # 이 경우 기존 거리가 더 작으니 그냥 볼 것도 없음
    for next in graph[cur]:
      cost=dist+next[1]
      if(distance[next[0]]>cost):
        distance[next[0]]=cost
        heapq.heappush(q,(cost,next[0]))
daik(1)
for i in range(1,n+1):
    if(i==INF):
        print(-1)
    else:
       print(distance[i])