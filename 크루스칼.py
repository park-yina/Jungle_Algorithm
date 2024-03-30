import sys
# 이 코드는 간접비용순으로 비교 한 뒤 사이클을 확인하는 방식의 크루스칼 알고리즘 구현코드입니다.
# 사이클이 없으면 최소신장 트리에 포함하고 사이클이 있다면 보지 않습니다
# 사이클이 있는지 없는지를 판별하는 방법은 바로 부모가 같은지 아닌지를 확인하는 방법입니다
# 이떄 대표자가 되는 기준은 좀 더 작은 쪽을 기준으로 합쳐야 작업을 하기 편합니다.

# 부모 테이블 초기화하기
# 필요한 함수 정리
# 1번 초기화 함수
# 2번 부모 찾기 함수
# 3번 집합 합치기 함수
# 간선 정보를 담을 리스트와 간선 정보 토대로 정렬할 함수
# 최종적으로 크루스칼 하는함수
# 최종함수에는 부모 다르면 합치고 최소신장에 넣고 가격 올리는 내용이 필요
v,e=map(int,input().split())
parent=[0]*(v+1)
for i in range(v+1):
    parent[i]=i
# 부모 테이블을 초기화하는 과정에서 크루스칼은 처음에는 자기 자신의 인덱스를 잡는다
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
        # 부모가 자기 자신이 아닐경우 재귀를 활용하여 경로를 압축하고 부모를 찾아간다
    return parent[x]
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if(a<b):
        parent[b]=a
    else:
        parent[a]=b
edges=[]
total=0
for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))
edges.sort()
for i in range(e):
    cost,a,b=edges[i]
    if(find_parent(parent,a)!=find_parent(parent,b)):
        union_parent(parent,a,b)
        total+=cost
print(total)
