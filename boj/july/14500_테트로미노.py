# # 5가지 종류의 테트로미노
# #
# # 자기 자신 기준 상하좌우 중 하나로 계속 연결하며 재귀호출
# # [i][j] 이면 [i+1][j] [i-1][j] [i][j+1] [i][j-1]
# # 이렇게 4개가 연결된 모든 경우를 따져서 최댓값 찾기
# #
# # 세로 n, 가로 m
#
# n, m = map(int, input().split())
# data = []
# result = []
# for i in range(n):
#     v = list(map(int, input().split()))
#     data.append(v)
#
# # 재귀함수
# def find(i, j, tmp, count):
#     tmp += data[i][j]
#     count += 1
#
#     if count == 4:
#         result.append(tmp)
#         return
#
#     if i < n - 1:
#         find(i + 1, j, tmp, count)
#     if 0 < i:
#         find(i - 1, j, tmp, count)
#     if j < m - 1:
#         find(i, j + 1, tmp, count)
#     if 0 < j:
#         find(i, j - 1, tmp, count)
#
#     # if count == 3:
#
# for i in range(n):
#     for j in range(m):
#         tmp, count = 0, 0
#         find(i, j, tmp, count)
#
# print(max(result))
# # 4개가 연결되게 재귀호출 하니까 ㅗ 모양을 체크 못하는 듯 (ㅗ 모양은 중간 얘랑 연결되는 거니까,,)



# 모범답안 참고

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

# 방문처리용
visited = [[False] * m for _ in range(n)]
# 상, 하, 좌, 우
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 최댓값
maxValue = 0

# ㅗ를 제외한 4개의 모양 최댓값 계산
def find_four(i, j, sum, cnt):
    global maxValue

    # 모양 완성
    if cnt == 4:
        maxValue = max(maxValue, sum)
        return

    # 이동하며 도형 만들기
    for k in range(4):
        move_i = i + move[k][0]
        move_j = j + move[k][1]
        if 0 <= move_i < n and 0 <= move_j < m and not visited[move_i][move_j]:
            # 방문표시
            visited[move_i][move_j] = True
            find_four(move_i, move_j, sum + data[move_i][move_j], cnt + 1)
            # 방문표시 제거
            visited[move_i][move_j] = False

# ㅗ 모양의 최댓값 계산
def find_one(i, j):
    global maxValue
    for k in range(4):
        # 초기값은 시작지점
        tmp = data[i][j]
        for l in range(3):
            # move 배열의 요소를 3개씩 사용
            # 00 01 02 // 10 11 12 // 20 21 22 // 30 31 32 => 0 1 2 // 1 2 3 // 2 3 0 // 3 0 1
            t = (k + l) % 4
            move_i = i + move[t][0]
            move_j = j + move[t][1]

            if not (0 <= move_i < n and 0 <= move_j < m):
                tmp = 0
                break
            tmp += data[move_i][move_j]

            # 최대값 계산
            maxValue = max(maxValue, tmp)

for i in range(n):
    for j in range(m):
        # 시작점 방문처리
        visited[i][j] = True
        find_four(i, j, data[i][j], 1)
        visited[i][j] = False

        find_one(i, j)

print(maxValue)