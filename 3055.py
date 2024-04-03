import sys
from collections import deque
input=sys.stdin.readline
r,c=list(input().split())
map_=[list(input().rstrip()) for _ in range(r)]
visit=[[-1]*c for _ in range(r)]
dx=[0,1,-1,0]
dy=[1,0,0,-1]
q=deque()
def bfs():
    while q:
        x,y=q.popleft()
        visit[0][0]=0
        if map_[x][y]=='S':
            return visit[x][y]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if(0<=nx<r and 0<=ny<c):
                #범위 내에 있을 때에 고슴도치가 안전할 수 있는 경우는 nx,ny가 빈곳이거나 비버집
                if(map_[nx][ny]=='.' or map_[nx][ny]=='D')and map_[x][y]=='S':
                    map_[nx][ny]=='S'
                    visit[nx][ny]=visit[x][y]+1
                    q.append(nx,ny)
                elif(map_[nx][ny]=='.' or map_[nx][ny]=='*')and map_[x][y]=='*':
                    map[nx][ny]='*'
                    q.append(nx,ny)
    return "KAKTUS"
for x in range(r):
    for y in range(c):
        if map_[x][y] == 'S':
            q.append((x,y))
        elif map_[x][y] == 'D':
            Dx,Dy = x,y

for x in range(r):
    for y in range(c):
        if map_[x][y] == '*':
            q.append((x,y))

print(bfs(Dx,Dy))
