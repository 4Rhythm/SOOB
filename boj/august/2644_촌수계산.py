# 부모 - 자식 1촌 / 나 - 아버지 1촌
# 아버지 - 할아버지 1촌 / 아버지 형제들 - 할아버지 1촌
# 나 - 할아버지 2촌
# 나 - 아버지 형제들 3촌

# 1, 2, 3, ... , n 의 연속된 번호
# 전체 사람 수 n
# 촌수 계산해야 되는 서로 다른 두 사람의 번호 a, b
# 부모 자식들 관계의 개수 m
# x, y => y의 부모 번호 = x

# 1차 풀이 생각: a, b 각각 가장 위 부모 노드를 구하고 부모 노드까지의 거리를 구함(1촌, 2촌..) => 그 둘 더하면 될 듯

# 2차 풀이 생각: 가장 위 부모 노드 구하는게 아니고 공통 부모 노드를 구해야 함.. dfs 말고 bfs로 다시 해보자
# 그 값이 속해있는 라인을 찾아보고 없으면 그 위의 부모노드 라인을 찾아보며 계속 위로 올라가기



# 1차 dfs 틀린 풀이
# from collections import deque
#
# n = int(input())
# a, b = map(int, input().split())
# m = int(input())
#
# graph = [[] for i in range(n + 1)]
#
# for i in range(m):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#
# def dfs(v):
#     global count
#     global q
#
#     for i in range(n + 1):
#         if v in graph[i]:
#             count += 1
#             q.append(i)
#             dfs(i)
#
# # 초기화
# count = 0
# q = deque()
# dfs(a)
# if len(q) != 0:
#     a_parents = q.pop()
#     a_count = count
# else:
#     a_parents = a
#     a_count = 0
#
# # 초기화
# count = 0
# q = deque()
# dfs(b)
# if len(q) != 0:
#     b_parents = q.pop()
#     b_count = count
# else:
#     b_parents = b
#     b_count = 0
#
# if a_parents != b_parents:
#     print(-1)
# else:
#     print(a_count + b_count)



# 2차 bfs 틀린 풀이
# 반례: https://www.acmicpc.net/board/view/33045
# 2번 이상 건너 있는 노드를 못 찾아서 틀림

# from collections import deque
#
# n = int(input())
# a, b = map(int, input().split())
# m = int(input())
#
# graph = [[] for i in range(n + 1)]
#
# for i in range(m):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#
# def bfs(a, b):
#     queue = deque()
#     count = 0
#     not_found = 0
#     queue.append(a)
#
#     while queue:
#         a = queue.pop()
#
#         if a == b:
#             not_found = -1
#             break
#
#         for i in range(n + 1):
#             if a in graph[i]:
#                 if b in graph[i]:
#                     count += 2
#                 else:
#                     queue.append(i)
#                     count += 1
#                     not_found += 1
#
#     if not_found == count:
#         return -1
#     else:
#         return count
#
# case_a = bfs(a, b)
# case_b = bfs(b, a)
#
# if case_a == -1 and case_b == -1:
#     print(-1)
#
# else:
#     if case_a > case_b:
#         print(case_a)
#     else:
#         print(case_b)



# 풀이 참고
# dfs, bfs 둘 다 가능한 문제

# bfs 풀이
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    # 양방향 그래프
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):
    queue = deque()
    queue.append(start)

    visited[start] = 1

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                visited[i] += (visited[node] + 1)
                queue.append(i)
bfs(a)

if visited[b] != 0:
    print(visited[b] - 1) # 자기 자신부터 셌기 때문에 -1
else:
    print(-1)

