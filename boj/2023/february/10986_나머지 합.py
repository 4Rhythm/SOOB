# 수 n개, 연속된 부분 구간 합이 m으로 나누어 떨어지는 구간의 개수 구하기
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# num = list(map(int, input().split()))
# prefix_sum = []
# tmp = 0
# for i in num:
#     tmp += i
#     prefix_sum.append(tmp)
# print(prefix_sum)

# 풀이 참고
# prefix sum에서 부분 합을 구하려면 P[j] - P[i - 1]의 과정
# P[j]와 P[i-1]이 각각 M으로 나눴을 때의 나머지가 동일하다면 => 빼기 연산 후 나머지는 0이 돼 M으로 나눠떨어지게 됨
# 결국 m으로 나누어떨어지는 부분합을 구하는 것 = 나머지가 동일한 idx 중 임의로 2개 조합(iP2) 선택하는 것
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
remainder_count = [0] * m # 나머지이므로 m 미만 => 0 1 .. m - 1

tmp = 0
for i in range(n):
    tmp += num[i]
    r = tmp % m
    remainder_count[r] += 1

answer = remainder_count[0] # 나머지가 0인 인덱스는 2개를 뽑지 않고 하나만 뽑아도 0으로 나누어 떨이지기 때문
for i in remainder_count:
    answer += i * (i - 1) // 2

print(answer)
