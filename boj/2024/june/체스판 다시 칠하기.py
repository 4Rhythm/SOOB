# MN개의 단위 정사각형으로 나누어져 있는 M x N 보드
# 어떤 정사각형은 검은색, 나머지는 흰색
# 보드 잘라서 8 x 8 크기의 체스판으로 만들려고 함
# 체스판은 검은색과 흰색이 번갈아 칠해져 있어야 함
# 다시 칠해야 하는 정사각형 개수의 최솟값을 출력

# 체스판 경우의 수는 두 가지
# 1. 맨 왼쪽 상단이 흰색
# 2. 맨 왼쪽 상단이 검은색

# (0, 0)부터 가능한 모든 8 x 8 체스판 하나를 완성된 두 개의 체스판과 비교하기

M, N = map(int, input().split())
board = []
limit, answer = 8, 8*8

for _ in range(M):
    line = input()
    board.append(line)

print('board', board) # board ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBBBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

W = "WBWBWBWB"
B = "BWBWBWBW"

start_white, start_black = [], []
sw, sb = True, True

for i in range(limit):
    if sw:
        start_white.append(W)
        sw = False
    else:
        start_white.append(B)
        sw = True

for i in range(limit):
    if sb:
        start_black.append(B)
        sb = False
    else:
        start_black.append(W)
        sb = True

print('start_white', start_white) # start_white ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
print('start_black', start_black) # start_black ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']


possible = []
for i in range(0, (M + 1) - limit):
    for j in range(0, (N + 1) - limit):
        possible.append([i, j])

for p in possible:
    tmp = []
    a, b = p[0], p[1]
    for i in range(a, a + limit):
        tmp.append(board[i][b:b+limit])
    print('tmp:', tmp)

    check_white, check_black = 0, 0
    for i in range(0, limit):
        print(tmp[i], start_black[i])

        for c1, c2 in zip(tmp[i], start_white[i]):
            if c1 != c2:
                check_white += 1

        for c1, c2 in zip(tmp[i], start_black[i]):
            if c1 != c2:
                check_black += 1

    tmp_check = min(check_white, check_black)
    answer = min(answer, tmp_check)

print(answer)