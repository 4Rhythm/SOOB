# 고속도로 위에 n개의 센서
# 최대 k개의 집중국

n = int(input())
k = int(input())
node = list(map(int, input().split()))
node.sort(reverse=True)

d = []
for i in range(0, n - 1):
    tmp = node[i] - node[i + 1]
    d.append(tmp)
d.sort()

answer = 0
for i in range(0, n - k):
    answer += d[i]
print(answer)