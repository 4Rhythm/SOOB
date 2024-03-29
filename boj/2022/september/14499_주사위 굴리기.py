# n x m 지도
# 지도의 오른쪽은 동쪽, 위쪽은 북쪽
# 지도 좌표 (r, c) // r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수
# 지도의 각 칸에는 정수가 하나씩 적혀있음
# 주사위를 굴렸을 때
#   1. 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
#   2. 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0

# 주사위: 지도 위의 윗면 1, 동쪽 3 // 놓인 곳은 (x, y) // 맨 처음엔 모든 면 0

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4

# 주사위 놓은 곳의 좌표와 이동 명령에 따라 상단에 쓰여 있는 값을 구하기

n, m, x, y, k = map(int, input().split())

graph = []
order = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

tmp = list(map(int, input().split()))
order.append(tmp)



