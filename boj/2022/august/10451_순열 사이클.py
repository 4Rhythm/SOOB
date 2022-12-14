# t: 테스트 케이스의 수
# n = 순열의 크기
#
# (1 2 3 4 5 6 7 8)
# (3 2 7 8 1 4 5 6)
#
# 1->3, 2->2 ...
#
# t번 함수를 호출하고, 호출 할 때마다 결과(순열 사이클의 개수)를 차곡차곡 저장하여 마지막에 출력하기

def setting(n, numbers):
    global graph
    global visited

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for i in range(n):
        graph[i + 1].append(numbers[i])

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = cycle # visited를 변수 cycle로 채움 => visited = [1, 2, 1, 1, 3] // 이렇게 되면 3이 토탈 사이클 수
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

result = [] # 각 순열 사이클의 개수를 저장하는 리스트
t = int(input())

for i in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))

    # 순열의 크기와, 순열을 토대로 세팅 (graph와 visited)
    setting(n, numbers)

    j = 1 # 순열 사이클 확인 count 변수, (1부터 n까지)
    cycle = 0 # 사이클의 토탈 개수

    while j != (n + 1):
        if visited[j] == False:
            cycle += 1
            dfs(graph, j, visited)
        else:
            pass
        j += 1

        if j == n + 1:
            break

    result.append(cycle) # 현재 cycle 값이 결국 토탈 개수이므로

    """ 이렇게 할 필요가 없었다.
    visited = map(int, visited) # False는 0 True는 1이므로 map(int, 리스트)를 통해 visited 안의 값들을 전부 숫자로 바꿔주기 위함
    value = max(visited)

    result.append(value)
    """

for i in result:
    print(i)
