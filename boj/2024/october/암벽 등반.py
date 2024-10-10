# 어떤 암벽에 n(1 ≤ n ≤ 50,000)개의 홈
# 각각의 홈의 좌표는 (x, y)
# |a - x| ≤ 2이고 |b - y| ≤ 2이면 (x, y)에서 (a, b)로 이동할 수 있음

# 이와 같이 홈들을 이용하여 이동하면서 y = T(1 ≤ T ≤ 200,000)일 때까지, 즉 암벽의 정상까지 오르려고 함

# 현재 위치는 (0, 0)
# 이동 회수를 최소로 하면서 정상에 오르려고 함
# 정상에 오를 때의 x좌표는 아무 것이나 되어도 상관이 없음

# 입력
# 첫째 줄에 n, T
# 다음 n개의 줄에는 각 점의 x, y좌표가 주어짐
# 두 좌표는 모두 0이상이며, x좌표는 1,000,000이하, y좌표는 T이하

# 출력
# 첫째 줄에 최소 이동 회수를 출력한 만약, 정상에 오를 수 없으면 -1을 출력

# 5 3
# 1 2
# 6 3
# 4 1
# 3 2
# 0 2

# from collections import deque
# import sys
#
# input = sys.stdin.readline
#
# n, T = map(int, input().split())
#
# visited = [False for _ in range(n)]
# points = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     points.append((x, y))
#
# points.sort(key=lambda x: (x[1], x[0]))
#
# start, end = 0, 0
# count = 0
#
# queue = deque([(start, end, count)])
#
# while queue:
#     now_x, now_y, now_count = queue.popleft()
#
#     if now_y == T:
#         print(now_count)
#         exit()
#
#     for i in range(n):
#         if not visited[i]:
#             tmp_x, tmp_y = points[i]
#             if abs(now_x - tmp_x) <= 2 and abs(now_y - tmp_y) <= 2:
#                 queue.append((tmp_x, tmp_y, now_count + 1))
#
# print(-1)


from collections import deque
import sys

input = sys.stdin.readline

n, T = map(int, input().split())

visited = set()
points = set()

for _ in range(n):
    x, y = map(int, input().split())
    points.add((x, y))

start, end = 0, 0
count = 0

queue = deque([(start, end, count)])

while queue:
    now_x, now_y, now_count = queue.popleft()

    if now_y == T:
        print(now_count)
        exit()

    for next_x in range(now_x - 2, now_x + 3):
        for next_y in range(now_y - 2, now_y + 3):
            if (next_x, next_y) in points and (next_x, next_y) not in visited:
                queue.append((next_x, next_y, now_count + 1))
                visited.add((next_x, next_y))

print(-1)