# 톱니바퀴 4개
# N극 0, S극 1
# k 회전 수
# a 회전 시킨 톱니바퀴, b 방향 (1 시계, -1 반시계)

# 맞닿은 곳은 항상 1의 2번, 2의 6번, 2의 2번, 3의 6번, 3의 2번, 4의 6번
# 극이 달라야 반대 방향으로 회전함

from collections import deque

# 참고) 톱니바퀴들을 딕셔너리 {}에 저장하자
# {1: deque([1, 0, 1, 0, 1, 1, 1, 1]), 2: deque([0, 1, 1, 1, 1, 1, 0, 1]), 3: deque([1, 1, 0, 0, 1, 1, 1, 0]), 4: deque([0, 0, 0, 0, 0, 0, 1, 0])}
gear = {}

for i in range(1, 5):
    tmp = input()
    gear[i] = deque(map(int, str(tmp)))
print(gear)

k = int(input())

def spin_left(a, b):
    if a < 1:
        return
    if gear[a][2] == gear[a + 1][6]:
        return

    spin_left(a - 1, -b)

    # 참고) roate함수를 사용하자(음수: 반시계 방향 회전, 양수: 시계 방향 회전)
    gear[a].rotate(b)

def spin_right(a, b):
    if a > 4:
        return
    if gear[a][6] == gear[a - 1][2]:
        return

    spin_left(a + 1, -b)
    gear[a].rotate(b)


for i in range(k):
    a, b = map(int, input().split())
    spin_left(a - 1, -b)
    spin_right(a + 1, -b)
    gear[a].rotate(b)

answer = 0
for i in range(4):
    answer += gear[i + 1][0] * (2**i)
print(answer)