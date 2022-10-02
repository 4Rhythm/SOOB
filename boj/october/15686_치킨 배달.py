# # n x n 도시
# # 1 x 1 칸: 빈 칸 0, 집 1, 치킨집 2
# # r, c => r행 c열 = 위에서부터 r, 왼쪽부터 c // 각각 1부터 시작
#
# # 치킨 거리: 집과 가장 가까운 치킨집 사이 거리
# # 도시의 치킨 거리: 모든 집의 치킨 거리의 합
#
# # 폐업 시키지 않을 치킨집 M개
# import copy
# import itertools
#
# n, m = map(int, input().split())
# city = []
# chicken = []
# home = []
#
# for _ in range(n):
#     tmp = list(map(int, input().split()))
#     city.append(tmp)
# print(city)
#
# no_chicken_city = copy.deepcopy(city)
#
# for i in range(n):
#     for j in range(n):
#         if city[i][j] == 1:
#             home.append((i, j))
#         elif city[i][j] == 2:
#             chicken.append((i, j))
#             no_chicken_city[i][j] = 0
# print(home)
# print(chicken)
# print(no_chicken_city)
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# # m개의 치킨집
# m_chicken = list(itertools.combinations(chicken, m))
# print(m_chicken)
#
# # def bfs():



from itertools import combinations
n, m = map(int,input().split())

city = []
home = []
chicken = []
answer = 999999

for _ in range(n):
    city.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i, j))
        if city[i][j] == 2:
            chicken.append((i, j))

m_chicken = list(combinations(chicken, m))
# print(m_chicken)

for c in m_chicken:
    tmp = 0 # 도시의 치킨 거리
    # print(c)

    for h in home:
        chicken_len = 999 # 각 집마다의 치킨 거리
        for k in range(m):
            chicken_len = min(chicken_len, abs(h[0] - c[k][0]) + abs(h[1] - c[k][1]))
        tmp += chicken_len
    answer = min(answer, tmp)

print(answer)