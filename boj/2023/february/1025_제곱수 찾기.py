# N행 M열
# 서로 다른 1개 이상의 칸 선택
# 행, 열 등차 수열

# 풀이 참고
from math import sqrt

n, m = map(int, input().split())
data = []

answer = -1

for _ in range(n):
    tmp = list(map(int, input().split()))
    data.append(tmp)

    for i in range(n): # i 행 위치
        for j in range(m): # j 시작 열 위치
            for a in range(-n, n): # a 행 등차
                for b in range(-m, m): # b 열 등차
                    num = ''
                    x, y = i, j

                    # 행과 열 시작 위치부터 등차를 더해가며 숫자 생성
                    while 0 <= x < n and 0 <= y < m:
                        num += data[x][y]
                        if a == 0 and b == 0:
                            break
                        if int(sqrt(int(num))) ** 2 == int(num):
                            answer = max(int(num), answer)
                        x += a
                        y += b
    print(answer)

