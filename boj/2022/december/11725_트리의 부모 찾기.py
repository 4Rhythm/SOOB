# 루트 없는 트리가 주어짐
# 트리의 루트 1
# 각 노드의 부모 구하기

# 1차 시도, 시간 초과
# from collections import deque
#
# num = int(input())
#
# node_list = []
# graph = [[] for _ in range(num)]
# visited = [0 for _ in range(num)]
#
# for _ in range(num - 1):
#     a, b = map(int, input().split())
#     node_list.append((a, b))
# # print(node_list)
#
# checkList = deque()
# checkList.append(1)
#
# while len(checkList) != 0:
#     c = checkList.popleft()
#
#     for i in range(num - 1):
#         if c in node_list[i] and visited[i] == 0:
#             a, b = node_list[i][0], node_list[i][1]
#
#             if a == c:
#                 graph[c].append(b)
#                 checkList.append(b)
#             else:
#                 graph[c].append(a)
#                 checkList.append(a)
#
#             visited[i] = 1
# # print(graph)
#
# for i in range(2, num + 1):
#     for j in range(1, num):
#         if i in graph[j]:
#             print(j)
#             continue



# 풀이 참고
from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    queue = deque()

    queue.append(1)
    visited[1] = 1

    while queue:
        node = queue.popleft()
        tmp = graph[node]

        for i in range(len(tmp)):
            new_node = tmp[i]
            if visited[new_node] == 0:
                visited[new_node] = node
                queue.append(new_node)

    for i in range(2, n + 1):
        print(visited[i])

bfs()
