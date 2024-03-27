
# 뱀 대가리를 늘린다는 것은 큐의 크기가 커진다는 걸까? 지금 큐를 뭐로 잡을까
# 만약 내가 도착한 곳에 사과가 있으면 사과의 개수는 하나 줄고 꼬리는 움직지지 않는다? 그럼 대가리는 움직이나
# 만약 이동한 칸에 사과가 없으면, 몸길이가 -1이 되고?
# 일단은 맵을 2차원 배열로 받아서 사과에 대한 부분을 체크하고 아 머리가 닿아야지 먹방을 찍을 수 있구나, 진짜 지능 문제다 
# 아 그러면 머리가 top이고 꼬리가 맨 뒤일테니까 둘 다 불러올 수 있는 자료구조가 필요할 것 같은데?
# 일단 사과는 1 기본map은 0 그러면 뱀 대가리가 또 따로 지정이 되어야하나? 근데 뱀이 사과를 먹는다는게 딱 대가리 끝에서 먹어야함???애매한 게 꼬리는 안움직인다는 게 뭔 뜻인지 모르겠어
# D는 오른쪽 돌기 L은 왼쪽돌기이다.
# 턴에는 조건이 있는데, 바로 오른쪽 왼쪽을 돌 때에 초가 함께 나온다는 것이다.
# 아마도 저 부분은 뱀의 꼬리랑 만나면 소용이 없는 거 같고 대가리랑 사과가 만나야 먹을 수 있는 거 가다.
# 그러면 뱀을 대가리랑 꼬리로 쪼개야 하는데 그럼 pair같은 자료형을 가지고 싶어요..코치님 저는 pair을 벡터에 넣고 싶습니다
# 
import sys
from collections import deque
n=int(input())
k = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
board = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):#사과의 위치
    x,y = map(int,input().split())
    board[x][y] = 1
info={}
command=int(input())
for _ in range(command):
    sec,dir=input().split()
    # 이렇게 쪼개는 이유는 몇초 뒤인지와 함께 방향 정보가 필요하기 때문이다
    info[int(sec)]=dir
cnt=0
x,y=1,1
board[x][y]=2
i=0
snake=deque([(1,1)])
while 1:
    nx=x+dx[i]
    ny=y+dy[i]
    if(nx<=0 or ny<=0 or nx>n or ny>n or ((nx, ny) in snake)):
        break
    if(board[nx][ny]!=1):
        l,r=snake.popleft()
        board[r][1]=0
    x,y=nx,ny
    board[x][y]=2
    snake.append((nx,ny))
    cnt+=1
    if(cnt in info.keys()):
        if info[cnt] == "D":
            d = (d+1)%4
        else:
            nd = 3 if d==0 else d-1
            d = nd
print(cnt+1)