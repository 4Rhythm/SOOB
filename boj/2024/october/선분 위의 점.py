# 문제
# 일차원 좌표상의 점 N개와 선분 M개
# 이때, 각각의 선분 위에 입력으로 주어진 점이 몇 개 있는지 구하기

# 입력
# 첫째 줄에 점의 개수 N과 선분의 개수 M (1 ≤ N, M ≤ 100,000)
# 둘째 줄에는 점의 좌표 (두 점이 같은 좌표를 가지는 경우는 없음)
# 셋째 줄부터 M개의 줄에는 선분의 시작점과 끝점
# 입력으로 주어지는 모든 좌표는 1,000,000,000보다 작거나 같은 자연수

# 출력
# 입력으로 주어진 각각의 선분 마다, 선분 위에 입력으로 주어진 점이 몇 개 있는지 출력

# n, m = map(int, input().split())
# point = list(map(int, input().split()))
# line = []
# for _ in range(m):
#     a, b = map(int, input().split())
#     line.append((a, b))
#
# for l in line:
#     answer = 0
#     for p in point:
#         if l[0] <= p <= l[1]:
#             answer +=1
#     print(answer)

# 5 1
# 1 3 10 20 30
# 2 15

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

points = list(map(int, input().split()))
points.sort()

lines = [list(map(int, input().split())) for _ in range(M)]

def find_location(x, check):
    start = 0  # 시작 위치
    end = len(points) - 1  # 끝 위치

    if check == 's':
        while start <= end:
            mid = (start + end) // 2

            if points[mid] >= x:
                end = mid - 1
            else:
                start = mid + 1

        return start

    elif check == 'e':
        while start <= end:
            mid = (start + end) // 2

            if points[mid] <= x:
                start = mid + 1
            else:
                end = mid - 1

        return end

for l in lines:
    start_idx = find_location(l[0], 's')
    end_idx = find_location(l[1], 'e')

    print(end_idx - start_idx + 1)