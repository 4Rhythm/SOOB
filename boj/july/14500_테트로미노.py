# 5가지 종류의 테트로미노
#
# 자기 자신 기준 상하좌우 중 하나로 계속 연결하며 재귀호출
# [i][j] 이면 [i+1][j] [i-1][j] [i][j+1] [i][j-1]
# 이렇게 4개가 연결된 모든 경우를 따져서 최댓값 찾기
#
# 세로 n, 가로 m

n, m = map(int, input().split())
data = []
result = []
for i in range(n):
    v = list(map(int, input().split()))
    data.append(v)

# 재귀함수
def find(i, j, tmp, count):
    tmp += data[i][j]
    count += 1

    if count == 4:
        result.append(tmp)
        return

    if i < n - 1:
        find(i + 1, j, tmp, count)
    if 0 < i:
        find(i - 1, j, tmp, count)
    if j < m - 1:
        find(i, j + 1, tmp, count)
    if 0 < j:
        find(i, j - 1, tmp, count)

    # if count == 3:


for i in range(n):
    for j in range(m):
        tmp, count = 0, 0
        find(i, j, tmp, count)

print(max(result))
# 4개가 연결되게 재귀호출 하니까 ㅗ 모양을 체크 못하는 듯 (ㅗ 모양은 중간 얘랑 연결되는 거니까,,)