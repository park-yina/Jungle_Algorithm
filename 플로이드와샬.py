import sys
input = sys.stdin.readline
n,v=int(input())
INF=987654321
graph=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(v):
    s,e,cost=map(int,input().split())
    graph[s][e]=cost
for i in range(1,n+1):
    graph[i][i]=0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])#직접 가는 것이 빠른지 하나 걸치는 게 더 빠른지

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if graph[i][j] == INF :
            print("0", end=" ")
        else :
            print(graph[i][j], end=" ")
    print()