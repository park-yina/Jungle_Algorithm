from collections import deque

def bfs(graph,node,visit):
    queue=deque([node])
    visit[node]=True
    while queue:
        v=queue.popleft()#c++에서는 그냥 pop이지만 파이썬에서는 스택과의 차이를 두기 위해 이런 식으로 사용
        print(v, end = ' ')

        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i]=True

graph = [
    [],
    [2, 3],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]

# 노드별로 방문 정보를 리스트로 표현
visited = [False] * 9

# 정의한 BFS 메서드 호출(노드 1을 탐색 시작 노드로 설정)
bfs(graph, 1, visited)

# from collections import deque

# def bfs(graph, start):
#     queue = deque([(start, 0)])  # 큐에 (노드, 거리) 튜플을 저장
#     visited = set()  # 방문한 노드를 저장하는 집합
#     while queue:
#         node, distance = queue.popleft()
#         print(node, end=' ')
#         visited.add(node)
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 queue.append((neighbor, distance + 1))  # 다음 노드와 거리를 큐에 추가

# graph = [
#     [],
#     [2, 3],
#     [1, 8],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7, 8],
#     [6, 8],
#     [2, 6, 7]
# ]

# # 정의한 BFS 메서드 호출(노드 1을 탐색 시작 노드로 설정)
# bfs(graph, 1)
