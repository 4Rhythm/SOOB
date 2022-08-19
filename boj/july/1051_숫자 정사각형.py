# n x m 직사각형, n과 m은 50보다 작거나 같은 자연수
# 각 칸에는 한 자리 숫자
# 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형 찾기

n, m = map(int, input().split())
data = []

# 최대 길이
if n >= m:
    max_len = n
else:
    max_len = m

for i in range(n):
    d = input()
    d_list = tuple(map(int, d))
    # print(d_list)
    data.append(d_list)

# 최대 가능한 길이부터 -1씩 내려가며 가능한지 찾기
while max_len > -1:
    for i in range(0, n):
        for j in range(0, m):
            move_i = i + (max_len - 1)
            move_j = j + (max_len - 1)
            if move_i <= n - 1 and move_j <= m - 1:
                tmp = data[i][j]
                if data[move_i][j] == tmp and data[i][move_j] == tmp and data[move_i][move_j] == tmp:
                    print(max_len**2)
                    max_len = -1
                    break
            else:
                break
        if max_len == -1:
            break
    if max_len != -1:
        max_len -= 1
    elif max_len == -1:
        break