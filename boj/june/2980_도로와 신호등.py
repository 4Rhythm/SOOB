# 상근은 1초에 1미터
# 신호등 개수 N, 길이 L
# D는 위치, R은 빨간색, G는 초록색이 지속되는 시간

# 2개 길이 10
# D는 위치
# 시작 0 0 3 0 5 0 0 0 0 0
# 첫번째 신호등은 RRRRR GGGGG RRRRR GGGGG
# 두번째 신호등은 RR GG RR GG RR GG

n, l = map(int, input().split())
p = 0 # 상근의 위치
time = 0 # 걸리는 시간
light = [] # 신호등 정보 리스트

for _ in range(n):
    value = list(map(int, input().split()))
    light.append(value)

while p != l:
    time += 1
    c = 1
    for i in light:
        if i[0] == p + 1:
            if 1 <= time % (i[1] + i[2]) <= i[1]:
                c = 0
            else:
                c = 1
            break
    if c == 1:
        p += 1

print(time-1)