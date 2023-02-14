# 3번부터 N + 2번 입장 번호
# 한 학생에게 출석 코드 보내면, 해당 학생은 본인의 입장 번호의 배수인 학생들에게 보냄
# K명의 졸고 있는 학생들은 제출 X, 보내지도 않음
#
# 무작위로 한 명이 학생에게 보내는 행위 Q번 반복 => 특정 구간의 입장 번호를 받은 학생들 중 출석 되지 않은 학생 구하기
import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
k_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))
check_list = list(set(q_list) - set(k_list))

check = [0 for _ in range(n + 3)]

for i in check_list:
    for j in range(i, n + 3, i):
        if j not in k_list:
            check[j] = 1

for i in range(3, n + 3):
    check[i] = check[i - 1] + check[i]

for _ in range(m):
    start, end = map(int, input().split())
    total = end - start + 1

    print((total - (check[end] - check[start - 1]))) # check[end] - check[start - 1] # 범위 이내 출석이 된 학생 => total에서 빼주면 출석 안된 학생







# '3' 4 '5' '6' ?7? 8 '9' '10' 11 '12'


