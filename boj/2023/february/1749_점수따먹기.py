# n * m 행렬, 각 칸에 -10000 ~ 10000
# 행렬의 부분 행렬을 그려 그 안에 적힌 정수의 합 구하는 게임
# 최대의 합 구하기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    data.append(tmp)

prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

# 누적합 구하기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + data[i - 1][j - 1] - prefix_sum[i - 1][j - 1]

# 부분합 계산 (max 연산)
answer = -400000000
for x1 in range(1, n + 1):
    for y1 in range(1, m + 1):
        for x2 in range(x1, n + 1):
            for y2 in range(y1, m + 1):
                answer = max(answer, prefix_sum[x2][y2] - prefix_sum[x2][y1 - 1] - prefix_sum[x1 - 1][y2] + prefix_sum[x1 - 1][y1 - 1])

print(answer)