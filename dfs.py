import sys
# 위 코드는 c++의 벡터를 사용하여 구현했던 코드를 파이썬 버전으로 바꾼 코드입니다.
# def dfs(graph, here, visit):
#     visit[here] = True
#     for i in graph[here]:
#         if not visit[i]:
#             dfs(graph, i, visit)

# graph = {
#     0: [1, 2],
#     1: [0, 3],
#     2: [0, 4],
#     3: [1],
#     4: [2]
# }

# visit = [False] * len(graph)

# dfs(graph, 0, visit)

# print(visit)

#아래 코드는 dfs를 파이썬에서 stack을 구현한 코드입니다.
# 시작 노드를 스택에 넣습니다.
# 스택이 비어 있지 않은 동안 다음을 반복합니다:
# 스택에서 노드를 꺼냅니다.
# 해당 노드를 방문하지 않았다면 방문 표시를 합니다.
# 인접한 노드들을 스택에 넣습니다.
# def dfs(graph, start):
#     visit = [False] * len(graph)
#     stack = [start]
#     while stack:
#         node = stack.pop()
#         if not visit[node]:
#             visit[node] = True
#             for next_node in reversed(graph[node]):
#                 if not visit[next_node]:
#                     stack.append(next_node)
#     return visit

# graph = {
#     0: [1, 2],
#     1: [0, 3],
#     2: [0, 4],
#     3: [1],
#     4: [2]
# }

# # DFS 호출
# result = dfs(graph, 0)
# print(result)
