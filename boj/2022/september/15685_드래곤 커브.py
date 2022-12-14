# x, y 시작점
# d 방향 (0 x증가, 1 y감소, 2 x감소, 3 y증가)
# g 세대
#
# x축→ y축↓
#
# K세대는 K-1세대를 끝점 기준으로 90도 시계 방향 회전 후 붙인 것
#
# 100 x 100 격자, n개의 드래곤 커브
#
# 구해야하는 것: 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 개수
#
# 1. 격자에 각각 드래곤 커브들 나타내기
#   1-1. 0세대부터 g세대까지 어떻게 그릴 것인지?
# 2. 정사각형 개수 세기



# 풀이 참조...
# 직접 회전을 구현하는 것이 아닌 규칙을 찾는 문제
# 0세대: 0(→)
# 1세대: 0 1
# 2세대: 0 1 2 1
# 3세대: 0 1 2 1 2 3 2 1
# 이전 세대의 방향 값들을 뒤집고 +1

n = int(input())

graph = [[0] * 101 for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    graph[x][y] = 1

    curve = [d]
    # g세대 만큼 반복
    for i in range(g):
        tmp = []
        for j in range(len(curve)):
            tmp.append((curve[-j - 1] + 1) % 4)
        curve.extend(tmp)

    # 드래곤 커브 생성
    for j in curve:
        nx = x + dx[j]
        ny = y + dy[j]
        graph[nx][ny] = 1

        x, y = nx, ny

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            answer += 1

print(answer)