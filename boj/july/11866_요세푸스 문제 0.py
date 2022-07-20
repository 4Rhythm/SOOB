# 1 ~ n 원을 이룸
# 양의 정수 k
# k번째 사람 제거 계속 반복

from collections import deque

n, k = map(int, input().split())

people = deque()
answer = []

for i in range(1, n+1):
    people.append(i)

while True:
    for i in range(k-1):
        tmp = people.popleft()
        people.append(tmp)
    pick = people.popleft()
    answer.append(pick)
    if len(people) == 0:
        break

answer = str(answer)
answer = "<" + answer[1:len(answer)-1] + ">"

print(answer)