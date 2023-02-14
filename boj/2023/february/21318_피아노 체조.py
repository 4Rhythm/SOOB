# n개의 악보, 1 ~ n번 번호
# 각 악보는 난이도 존재, 수 클수록 어려운 악보
#
# 1 <= x <= y <= n을 만족하는 두 정수 x, y를 골라 x ~ y번 악보 순서대로 연주
#
# 지금 연주하는 악보가 다음 악보보다 어렵다면 실수함
# 몇 번 실수하는지 구하기

import sys
input = sys.stdin.readline

n = int(input())
level = list(map(int, input().split()))
fail = [0 for _ in range(len(level) + 1)]
sum = 0
for i in range(0, len(level) - 1):
    if level[i] > level[i + 1]:
        sum += 1
    fail[i + 1] = sum
# print(fail)

q = int(input())
for _ in range(q):
    answer = 0
    x, y = map(int, input().split())
    print(fail[y - 1] - fail[x - 1])