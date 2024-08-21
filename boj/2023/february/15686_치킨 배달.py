# 크기 n * n 도시
# 도시의 각 칸은 빈 칸 0, 집 1, 치킨 집 2 중 하나 (r, c)
# 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리
# 모든 집의 치킨 거리 합이 최소 되어야 함
# 치킨집 중 최대 m개 고르기
from itertools import combinations

city = []
home = []
chicken = []
answer = 999999

n, m = map(int, input().split())

for _ in range(n):
    city.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i, j))
        if city[i][j] == 2:
            chicken.append((i, j))

m_chicken = list(combinations(chicken, m))

for c in m_chicken:
    tmp = 0 # 치킨 거리

    for h in home:
        chicken_len = 999
        for k in range(m):
            chicken_len = min(chicken_len, abs(h[0] - c[k][0]) + abs(h[1] - c[k][1]))
        tmp += chicken_len
    answer = min(answer, tmp)
print(answer)



