# 트리의 1번 정점에는 W물
# 1번을 제외한 모든 정점에는 물 X

# 매초마다 모든 정점은
#     1. 물을 가지고 있으며, 자식 정점이 있으면 자식 정점 중 하나를 골라 물을 1줌(확률은 동일하게)
#     2. 부모 정점이 자신에게 물을 흘려보냈다면 받아서 쌓아둠
#
# 더 이상 물이 움직이지 않는 상태가 되었을 때 각 정점에 어느 정도 물이 있는지
# i번 정점에 쌓인 물의 양의 기댓값 Pi
# 0보다 큰 Pi 가진 정점들의 평균 구하기



# => 리프 노드의 수 구하는 문제였음
import sys
from collections import deque

n, w = map(int, sys.stdin.readline().split())
visited = [False for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

check = deque()
check.append(1)
leaf = 0

while check:
    node = check.popleft()
    visited[node] = True

    cnt = 0
    for i in graph[node]:
        if visited[i] == False:
            cnt += 1
            check.append(i)
    if cnt < 1:
        leaf += 1

print(w / leaf)