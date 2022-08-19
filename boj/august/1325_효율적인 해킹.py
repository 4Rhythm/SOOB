# 신뢰하는 관계, 신뢰하지 않는 관계
# A가 B를 신뢰함 -> B 해킹하면 A도 해킹
#  = 방향 그래프 B -> A
import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# n은 컴퓨터 수, m은 신뢰 관계수
n, m = map(int, input().split())

# 맨 앞은 비워두고 1부터 시작
graph = [[] for _ in range(n + 1)]

count_list = [0] # 인덱스 1부터 체크하기 위해
answer = []

# 방향 그래프 요소 추가
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

# 각 컴퓨터마다 확인
for j in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(graph, j, visited)

    # count = 0
    # for k in visited: # 방문 가능한 컴퓨터의 개수를 통해 판단
    #     if k == True:
    #         count += 1

    count = visited.count(True)

    count_list.append(count)

# 최댓값
max_com = max(count_list)

# 최댓값과 동일한 다른 원소들 저장 (오름차순)
for i in range(1, n + 1):
    if count_list[i] == max_com:
        answer.append(i)

# # list에서 value 값으로 다중 index 찾기
# answer = list(filter(lambda x: count_list[x] == max_com, range(len(count_list))))

for i in answer:
    print(i, end=' ')