# 고슴도치 한 마리
# 고슴도치는 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 함
#
# 티떱숲의 지도는 R행 C열
# 비어있는 곳은 '.', 물이 차있는 지역은 '*', 돌은 'X'
# 비버의 굴은 'D', 고슴도치의 위치는 'S'
#
# 매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동 (위, 아래, 오른쪽, 왼쪽)
# 물도 매 분마다 비어있는 칸으로 확장
#
# 물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 됨
# 물과 고슴도치는 돌을 통과할 수 없음
# 고슴도치는 물로 차있는 구역으로 이동할 수 없음
# 물도 비버의 소굴로 이동할 수 없음
#
# 티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간
#
# 고슴도치는 물이 찰 예정인 칸으로 이동할 수 없음
# 즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없음
#
# 첫째 줄에 50보다 작거나 같은 자연수 R과 C가 주어짐
# 다음 R개 줄에는 티떱숲의 지도가 주어지며, 문제에서 설명한 문자만 주어짐
# 'D'와 'S'는 하나씩만 주어짐
#
# 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간 출력
# 안전하게 비버의 굴로 이동할 수 없다면, "KAKTUS" 출력

r, c = map(int, input().split())
nowX, nowY = 0, 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

map = []

time = 0

for i in range(r):
    tmp = list(input())

    if 'S' in tmp:
        nowX, nowY = i, tmp.index('S')

    map.append(tmp)

def cycle1():
    location = []

    for i in range(r):
        for j in range(c):
            if map[i][j] == 'S':
                location.append([i, j])

    if len(location) == 0:
        return False

    for l in location:
        nowX, nowY = l[0], l[1]

        for d in range(4):
            nextX = nowX + dx[d]
            nextY = nowY + dy[d]

            if 0 <= nextX < r and 0 <= nextY < c:
                if map[nextX][nextY] == 'D':
                    return True

                if map[nextX][nextY] == 'X' or map[nextX][nextY] == '*':
                    continue

                if map[nextX][nextY] == '.':
                    map[nextX][nextY] = 'S'

        map[nowX][nowY] = '.'

def cycle2():
    water = []
    for i in range(r):
        for j in range(c):
            if map[i][j] == '*':
                water.append((i, j))

    for w in water:
        wX, wY = w[0], w[1]

        for d in range(4):
            nX = wX + dx[d]
            nY = wY + dy[d]

            if 0 <= nX < r and 0 <= nY < c:
                if map[nX][nY] == 'D':
                    continue

                if map[nX][nY] != 'X':
                    map[nX][nY] = '*'

while True:
    time += 1
    result = cycle1()
    cycle2()

    if result is None:
        continue
    elif not result:
        print('KAKTUS')
        break
    else:
        print(time)
        break