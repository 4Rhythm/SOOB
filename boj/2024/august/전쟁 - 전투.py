# 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷
# 같은 팀의 병사들은 모이면 모일수록 강해짐
#
# N명이 뭉쳐있을 때는 N^2의 위력을 낼 수 있음
# 과연 지금 난전의 상황에서는 누가 승리할 것인가?
# 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않음
#
# 입력
# 첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어짐
# 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어짐
# 모든 자리에는 병사가 한 명 있음
# B는 파란색, W는 흰색
# 당신의 병사와 적국의 병사는 한 명 이상 존재함
#
# 출력
# 첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력함

# 입력
# 5 5
# WBWWW
# WWWWW
# BBBBB
# BBBWW
# WWWWW

from collections import deque

def find_W(startW_X, startW_Y):
    sumW = 0
    W_queue = deque([[startW_X, startW_Y]])
    graph[startW_X][startW_Y] = '0'

    while W_queue:
        tmp = W_queue.popleft()
        nowX, nowY = tmp[0], tmp[1]

        sumW += 1

        for i in range(4):
            newX = nowX + dx[i]
            newY = nowY + dy[i]

            if 0 <= newX < M and 0 <= newY < N:
                if graph[newX][newY] == 'W':
                    W_queue.append([newX, newY])
                    graph[newX][newY] = '0'
    return sumW

def find_B(startB_X, startB_Y):
    sumB = 0
    B_queue = deque([[startB_X, startB_Y]])
    graph[startB_X][startB_Y] = '0'

    while B_queue:
        tmp = B_queue.popleft()
        nowX, nowY = tmp[0], tmp[1]

        sumB += 1

        for i in range(4):
            newX = nowX + dx[i]
            newY = nowY + dy[i]

            if 0 <= newX < M and 0 <= newY < N:
                if graph[newX][newY] == 'B':
                    B_queue.append([newX, newY])
                    graph[newX][newY] = '0'
    return sumB

N, M = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(M):
    tmp = str(input())
    tmp_list = list(map(str, tmp))
    graph.append(tmp_list)

answerW, answerB = 0, 0

for i in range(M):
    for j in range(N):
        # print('i, j:', i, j)
        # for a in range(M):
        #     print(graph[a])
        # print()
        if graph[i][j] == 'W':
            tmp = find_W(i, j)
            answerW += (tmp * tmp)
        elif graph[i][j] == 'B':
            tmp = find_B(i, j)
            answerB += (tmp * tmp)
        else:
            continue
        # print('answerW, answerB: ', answerW, answerB)

print(answerW, answerB)