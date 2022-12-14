# 방향 그래프 G
# i에서 j로 가는 경로 있는지 없는지 구하는 문제

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        possible.append(i) # 도달할 수 있는 j 저장
        if not visited[i]:
            dfs(graph, i, visited)

n = int(input())

data = [] # (입력 받는) 그래프의 인접 행렬
graph = [[] for _ in range(n)]
# visited = [False] * n

answer = [[0 for j in range(n)] for i in range(n)]

# (입력 받는) 그래프의 인접 행렬
for i in range(n):
    tmp = list(map(int, input().split()))
    data.append(tmp)
# print(data)

# 인접 행렬 -> 인접 리스트 생성
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            graph[i].append(j)
# print(graph)

# dfs를 통해 하나의 i에서부터 도달 가능한 j들 찾아내기
for i in range(n):
    # print("i: %s" %i)
    possible = [] # 도달 가능한 j 담아내는 임시 리스트
    visited = [False] * n # i마다 초기화 시켜주기 위해 해당 위치에 선언

    dfs(graph, i, visited)

    # print(possible)

    for j in possible:
        if answer[i][j] == 0:
            answer[i][j] = 1
# print(answer)

for i in answer:
    i = str(i)
    i = i[1:len(i)-1]
    i = i.replace(",", "")

    print(i)



# 참고한 문법: 출력 부분, 문자열에서 쉼표 제거하기
# i = i.replace(",", "")