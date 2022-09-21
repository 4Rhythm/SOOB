# R행 x C열 격자판
# 각 칸에 미세먼지의 양을 실시간으로 모니터링

# 공기청정기는 항상 1열, 2개의 행에 걸쳐있음

# 1초 동안
#     1. 미세먼지 확산, 모든 칸에서 동시에
#         (r,c)에 있는 미세먼지 => 인접한 4방향으로 확산
#             인접한 방향에 공기청정기 있거나, 칸 없으면 확산 X
#
#         확산되는 양은 A(r,c)/5, 소수점은 버림
#         (r,c)에 남은 미세먼지 양 = A(r,c) - (A(r,c)/5) x (확산된 방향의 개수)
#
#     2. 공기청정기 작동
#         위쪽 공기청정기의 바람은 반시계 방향
#         아래쪽 공기청정기의 바람은 시계 방향
#
#         바람 불면 미세먼지가 바람 방향으로 모두 한 칸씩 이동
#
#         공기청정기로 들어간 미세먼지는 정화됨!

import copy
from math import trunc

r, c, t = map(int, input().split())
room = []

for _ in range(r):
    tmp = list(map(int, input().split()))
    room.append(tmp)

# print(room)

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(t):
    # 모든 칸에서 동시에 미세먼지 확산
    room_1 = copy.deepcopy(room)
    for i in range(r):
        for j in range(c):
            count = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < r and 0 <= ny < c:
                    if room[nx][ny] != -1:
                        room_1[nx][ny] += trunc(room[i][j] / 5)
                        count += 1
            room_1[i][j] -= trunc(room[i][j] / 5) * count
    # print(room_1)

    # 공기청정기 작동
    room_2 = copy.deepcopy(room_1)
    machine = []
    for i in range(r):
        for j in range(c):
            if room[i][j] == -1:
                machine.append([i, j])
    up_start = machine[0][0]
    down_start = machine[1][0]

    # 3 -> 0 -> 2 -> 1
    # 상 하 좌 우
    # d_list = [3, 0, 2, 1]
    # while (nx != up_start-1) or (ny != 0):

    # 위쪽
    # (up_start, 1) = 0!!
    # (up_start, 1)부터 (up_start, c - 2)까지는 우
    # (up_start, c - 1)부터 (1, c - 1) 까지는 상
    # (0, c - 1) 부터 (0, 1)까지는 좌
    # (0, 0)부터 (up_start - 2, 0)까지는 하
    # (up_start - 1, 0) = 0!!
    room_2[up_start][1] = 0
    for i in range(1, c - 1):
        room_2[up_start][i + 1] = room_1[up_start][i]
        # print(up_start, i)
    for i in range(up_start, 0, -1):
        room_2[i - 1][c - 1] = room_1[i][c - 1]
        # print(i, c - 1)
    for i in range(c - 1, 0, -1):
        room_2[0][i - 1] = room_1[0][i]
        # print(0, i)
    for i in range(0, up_start - 1):
        room_2[i + 1][0] = room_1[i][0]
        # print(i, 0)
    room_2[up_start - 2][0] = 0

    # 아래쪽
    # (down_start, 1) = 0!!
    # (down_start, 1)부터 (down_start, c - 2)까지는 우
    # (down_start, c - 1)부터 (r - 2, c - 1) 까지는 하
    # (r - 1, c - 1) 부터 (r - 1, 1)까지는 좌
    # (r, 0)부터 (down_start - 2, 0)까지는 상
    # (down_start - 1, 0) = 0!!
    room_2[down_start][1] = 0
    for i in range(1, c - 1):
        room_2[down_start][i + 1] = room_1[down_start][i]
        # print(down_start, i)
    for i in range(down_start, r - 1):
        room_2[i + 1][c - 1] = room_1[i][c - 1]
        # print(i, c - 1)
    for i in range(c - 1, 0, -1):
        room_2[r - 1][i - 1] = room_1[r - 1][i]
        # print(r-1, i)
    for i in range(r - 1, down_start + 1, -1):
        room_2[i - 1][0] = room_1[i][0]
        # print(i, 0)
    room_2[down_start + 1][0] = 0

    # for i in room_2:
    #     print(i)

    room = copy.deepcopy(room_2)

    answer = 0
    for i in room:
        answer += sum(i)

print(answer + 2)