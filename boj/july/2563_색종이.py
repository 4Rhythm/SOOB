# 1. 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리
# 2. 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리

white = [[0 for j in range(100)] for i in range(100)]

n = int(input())

for i in range(n):
    l, d = map(int, input().split())
    for j in range(l, l+10):
        for k in range(d, d+10):
            if white[j][k] == 0:
                white[j][k] = 1

white = sum(white, [])
print(white.count(1))