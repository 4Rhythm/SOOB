# 2차원 세계에 블록이 쌓여있음
# 비가 오면 블록 사이에 빗물이 고임
# 비는 충분히 많이 옴 고이는 빗물의 총량 구하기

# 첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어짐 (1 ≤ H, W ≤ 500)
# 두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.
# 따라서 블록 내부의 빈 공간이 생길 수 없음 또 2차원 세계의 바닥은 항상 막혀있다고 가정

# 2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.
# 빗물이 전혀 고이지 않을 경우 0을 출력하여라.

H, W = map(int, input().split())
block = list(map(int, input().split()))
water = 0

for i in range(1, W - 1):
    left = max(block[:i])
    right = max(block[i + 1:])
    tmp_water = min(left, right)

    if tmp_water > block[i]:
        water += tmp_water - block[i]

print(water)