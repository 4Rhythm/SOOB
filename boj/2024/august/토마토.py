# 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있음
# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 됨
# 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미함
# 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정함
#
# 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 함
#
# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하기
#
# 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있음
#
# 입력
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M, N
# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수
# 단, 2 ≤ M, N ≤ 1,000
#
# 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어짐
# 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어짐
#
# 1: 익은 토마토
# 0: 익지 않은 토마토
# -1: 토마토가 들어있지 않은 칸
#
# 토마토가 하나 이상 있는 경우만 입력으로 주어짐
#
# 출력
# 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 함
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력
# 토마토가 모두 익지는 못하는 상황이면 -1을 출력
from collections import deque

M, N = map(int, input().split())
box = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(N):
    tmp = list(map(int, input().split()))
    box.append(tmp)

yet = 0 # 아직 안 익은 개수
day = 0 # 날짜
queue = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1: # 익음
            queue.append((i, j, day))
        elif box[i][j] == 0: # 안익음
            yet += 1
        else:
            continue

# 저장부터 다 익어있는 케이스
if yet == 0:
    print(0)
    exit()

while queue:
    # print('queue: ', queue)
    node = queue.popleft()
    nowX, nowY, nowDay = node[0], node[1], node[2]

    # print('nowX, nowY, nowDay: ', nowX, nowY, nowDay)
    # print('yet now: ', yet)
    # print('박스 현 상태')
    # for i in range(N):
    #     print(box[i])
    # print()

    nextDay = nowDay + 1

    for i in range(4):
        nextX = nowX + dx[i]
        nextY = nowY + dy[i]

        if (0 <= nextX < N) and (0 <= nextY < M) and (box[nextX][nextY]) == 0:
            box[nextX][nextY] = 1
            yet -= 1

            if yet == 0:
                print(nextDay)
                exit()

            queue.append((nextX, nextY, nextDay))

if yet != 0:
    print(-1)