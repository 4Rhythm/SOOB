# # n x n 크기
# # 물고기 m, 아기 상어 1마리
# # 아기 상어 크기 2 시작
# #
# # 아기 상어는 자신의 크기보다 큰 물고기 칸은 지나갈 수 없음 => 작거나 같으면 지나갈 수 있음
# # 자신의 크기보다 작은 물고기만 먹을 수 있음 => 크기 같거나 크면 먹을 수 없음
# #
# # 더 이상 먹을 수 있는 물고기가 공간에 없다면 종료
# #
# # 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러 감
# #                    1마리 이상이라면 거리가 가장 가까운 물고기를 먹으러 감
# #                         지나야하는 칸의 개수 최솟값
# #                         거리 가까운 물고기가 많다면, 가장 위에 있는 물고기
# #                         그런 물고기가 많다면 가장 왼쪽에 있는 물고기
# #
# # 이동(먹는데 걸리는 시간은 없다고 가정) = 1초
# # 자신의 크기와 같은 수의 물고기를 먹으면 크기 1 증가
# from collections import deque
#
# # 상 좌 하 우
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# x, y = 0, 0
#
# n = int(input())
# space = []
#
# for _ in range(n):
#     tmp = list(map(int, input().split()))
#     space.append(tmp)
#
# for i in range(n):
#     for j in range(n):
#         if space[i][j] == 9:
#            x, y = i, j
#
# print(x, y)
# print(space)
#
# shark_size = 2
# next_size = 0
# eat = []
# time = 0
#
# queue = deque()
# queue.append((x, y))
#
# while True:
#     for i in range(n):
#         for j in range(n):
#             if space[i][j] < shark_size and space[i][j] != 0:
#                 eat.append((i, j))
#                 eat = list(set(eat))
#     print('eat:', eat)
#
#     if not eat:
#         print(time)
#         break
#
#     time_graph = [[0 for _ in range(n)] for _ in range(n)]
#
#     while queue:
#         print('eat:', eat)
#         print('time_graph:', time_graph)
#         print('queue:', queue)
#         node = queue.popleft()
#         x, y = node[0], node[1]
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             print("nx, ny: ", nx, ny)
#
#             if 0 <= nx < n and 0 <= ny < n:
#                 if time_graph[nx][ny] == 0:
#                     if (nx, ny) in eat:
#                         print("잡음", nx, ny)
#                         time_graph[nx][ny] = time_graph[x][y] + 1
#                         time += time_graph[nx][ny]
#                         space[nx][ny] = 0
#                         next_size += 1
#                         if shark_size == next_size:
#                             shark_size += 1
#                             next_size = 0
#                         eat.remove((nx, ny))
#                         queue.clear()
#                         queue.append((nx, ny))
#                         time_graph = [[0 for _ in range(n)] for _ in range(n)]
#                         print(queue)
#                         break
#
#                     else:
#                         if space[nx][ny] <= shark_size:
#                             time_graph[nx][ny] = time_graph[x][y] + 1
#                             queue.append((nx, ny))
#                             print(queue)
#             else:
#                 continue
#         print('hello')
#
#     queue.append((nx, ny))



# 답안 참조
import sys, collections

shark_x, shark_y = 0, 0
shark_size = 2 # 상어 크기
eat_cnt = 0 # 먹은 물고기 몇 마리?

fish_cnt = 0 # 물고기 몇 마리?
fish_pos = [] # 물고기들의 위치

time = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if 0 < board[i][j] <= 6:
            fish_cnt += 1
            fish_pos.append((i, j))
        elif board[i][j] == 9:
            shark_x, shark_y = i, j
board[shark_x][shark_y] = 0

def bfs(shark_x, shark_y):
    q = collections.deque([(shark_x, shark_y, 0)])
    dist_list = []
    visited = [[False] * n for _ in range(n)]
    visited[shark_x][shark_y] = True
    min_dist = int(1e9)
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] <= shark_size:
                    visited[nx][ny] = True
                    if 0 < board[nx][ny] < shark_size:
                        min_dist = dist
                        dist_list.append((dist + 1, nx, ny))
                    if dist + 1 <= min_dist:
                        q.append((nx, ny, dist + 1))
    if dist_list:
        dist_list.sort()
        return dist_list[0]
    else:
        return False

while fish_cnt:
    result = bfs(shark_x, shark_y)
    if not result:
        break

    shark_x, shark_y = result[1], result[2]
    time += result[0]
    eat_cnt += 1
    fish_cnt -= 1

    if shark_size == eat_cnt:
        shark_size += 1
        eat_cnt = 0

    board[shark_x][shark_y] = 0

print(time)