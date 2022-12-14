# n x n 보드, 사과 개수 k
# 뱀의 길이 1, 사과 먹으면 뱀 길이 증가
# 벽 또는 자기 자신의 몸과 부딪히면 게임 끝

from collections import deque

n = int(input())
k = int(input())

count = 0 # 초

snake_x, snake_y = 0, 0 # 처음 위치(머리의 위치) // 맨위 맨좌측

# 뱀이 위치하는 좌표 리스트
snake = deque([[snake_x, snake_y]])

# 머리 방향, 동 남 서 북(시계 방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

i, j = 0, 0 # 방향 인덱스
# head_x, head_y = dx[i], dy[j] # 처음엔 오른쪽(동)

board = [[0 for j in range(n)] for i in range(n)]

# 보드 위 뱀 표시
board[snake_x][snake_y] = 's'

# 보드 위 사과 표시
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 'a'

# 방향 리스트
direction = deque()
l = int(input())
for _ in range(l):
    tmp = list(map(str, input().split()))
    direction.append(tmp)

while True:
    count += 1
    move_x = snake_x + dx[i]
    move_y = snake_y + dy[j]

    # 벽에 부딪히거나 자기자신의 몸과 부딪히는 경우
    if move_x < 0 or n <= move_x or move_y < 0 or n <= move_y or board[move_x][move_y] == 's':
        break
    else:
        if board[move_x][move_y] == 'a':
            pass
        else:
            tmp = snake.popleft()
            board[tmp[0]][tmp[1]] = '0'

        board[move_x][move_y] = 's'
        snake.append([move_x, move_y])

        snake_x = move_x
        snake_y = move_y

    if len(direction) != 0:
        if direction[0][0] == str(count):
            if direction[0][1] == 'D':
                i = (i + 1) % 4
                j = (j + 1) % 4
            else:
                i = ((i - 1) + 4) % 4
                j = ((j - 1) + 4) % 4
            direction.popleft()

print(count)










