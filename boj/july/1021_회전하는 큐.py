# N개의 원소 포함 양방향 순환 큐
#
# 1. 첫 번째 원소 뽑아내기
# 2. 왼쪽으로 한 칸 이동 (맨 앞 원소는 맨 뒤로)
# 3. 오른쪽으로 한 칸 이동 (맨 뒤 원소는 맨 앞으로)
#
# 2번과 3번을 최소로 사용하여 뽑으려는 원소들이 맨 앞으로 오게
import math
from collections import deque

deq = deque()

count = 0

# 큐의 크기 n, 뽑으려는 수의 개수 m
n, m = map(int, input().split())
pick_deq = deque(map(int, input().split()))

for i in range(1, n+1):
    deq.append(i)

while m > 0:
    pick = pick_deq.popleft()
    position = deq.index(pick) + 1

    if position == 1:
        deq.popleft()
    elif position == len(deq):
        deq.pop()
        count += 1
    elif position <= math.ceil(len(deq) / 2):
        for _ in range(position):
            tmp = deq.popleft()
            deq.append(tmp)
            position -= 1
            count += 1
            if position == 1:
                deq.popleft()
                break
    else:
        for _ in range(len(deq)):
            tmp = deq.pop()
            deq.appendleft(tmp)
            position += 1
            count += 1
            if position == len(deq):
                deq.pop()
                count += 1
                break
    m -= 1
    if m == 0:
        break

print(count)


