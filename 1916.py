import sys
import heapq
INF=987654321
input=sys.stdin.readline
n=int(input())
m=int(input())
visit=[False]*(n+1)
distance=[INF]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
s,e=map(int,input().split()) #시작과 끝을 마지막으로 입력을 받는다
def cal():
  min=INF
  index=0
  for i in range(n+1):
    if(distance[i]<min and not visit[i]):
      visit[i]=True
      min=distance[i]
      index=i
    return index
def daik(s):
  distance[s]=0
  visit[s]=True
  for next in graph[s]:
        if(distance[next[0]]>next[1]):#최단거리보다 만약에 지난 거리더 거리가 짧으면
            distance[next[0]]=next[1]
    for

