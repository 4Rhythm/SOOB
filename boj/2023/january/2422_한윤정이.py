# 아이스크림 가게에는 N종류 아이스크림
# 특정 종류 아이스크림을 섞어먹지 않고 3가지 선택하는 경우의 수
import itertools

n, m = map(int, input().split())

numbers = []
for i in range(1, n + 1):
    numbers.append(i)
total_list = list(itertools.combinations(numbers, 3)) # 조합

graph = [[] for _ in range(n + 1)]
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in total_list:
    if i[1] in graph[i[0]] or i[2] in graph[i[0]]:
        continue
    if i[2] in graph[i[1]] or i[0] in graph[i[1]]:
        continue
    if i[0] in graph[i[2]] or i[1] in graph[i[2]]:
        continue
    answer += 1

print(answer)





# print(graph)
#
# print(total_list)
#
# for i in range(1, n + 1):
#
#
# for i in range(1, n + 1):
#     graph[i].append(i)
#     answer += math.comb(n - len(graph[i]) - 1, 2)
#
#
# print(answer / 2)

#
#
# 1 2 3 4 5
#
# 4 5
# 23 24 25 34 35