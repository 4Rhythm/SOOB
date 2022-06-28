import sys

n = 5
data = [sys.stdin.readline().strip() for i in range(n)]

high = 0
answer = []

for i in data:
    l = len(i)
    if high < l:
        high = l

for i in range(high):
    for j in range(n):
        if len(data[j]) < i + 1:
            continue
        else:
            answer.append(data[j][i])

answer = ''.join(map(str, answer))

print(answer)