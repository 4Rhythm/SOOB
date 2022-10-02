# 청소하는 영역의 개수 구하기

# n x m 크기, 1 x 1 칸 // (r, c)
# 각 칸은 벽(1) 또는 빈 칸(0)

# 청소기의 방향: 0북, 1동, 2남, 3서

# 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없음

# 1. 현재 위치 청소
# 2. 왼쪽부터 차례대로 탐색
#     1. 왼쪽에 청소하지 않은 공간이 있다면, 왼쪽으로 회전 후 한 칸 전진 => 1번으로 돌아가기
#     2. 없다면, 회전 후 => 2번으로 돌아가기
#     3. 네 방향 모두 청소 되어 있거나, 벽이라면 그대로 한 칸 후진하고 => 2번으로 돌아가기
#     4. 네 방향 모두 청소 되어 있거나, 벽이며, 후진도 불가능할 경우 작동 멈춤

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

place = []

n, m = map(int, input().split())

visited = [[0 for _ in range(m)] for _ in range(n)]
# print(visited)

r, c, d = map(int, input().split())

for m in range(n):
    tmp = list(map(int, input().split()))
    place.append(tmp)
# print(place)

# 1번 과정
def step_1(r, c):
    visited[r][c] = 1  # 방문처리

# 2번 과정
def step_2(r, c, d):
    for _ in range(4):
        d = (d - 1) % 4
        # print(d)
        nx = dx[d] + r
        ny = dy[d] + c

        # 해당 영역에 방문한 적이 없고 빈 칸일 경우
        if visited[nx][ny] == 0 and place[nx][ny] == 0:
            cleaning(nx, ny, d)
            return
        else:
            pass

def cleaning(r, c, d):

    step_1(r, c)
    step_2(r, c, d)

    # 4방향 모두 불가능한 경우
    # 방향은 유지한 채, 후진
    nd = (d - 2) % 4
    nx = dx[nd] + r
    ny = dy[nd] + c

    if place[nx][ny] == 1:
        answer = 0
        for i in visited:
            tmp = sum(i)
            answer += tmp
        print(answer)
        exit(0)
    else:
        cleaning(nx, ny, d)

# 실행
cleaning(r, c, d)

