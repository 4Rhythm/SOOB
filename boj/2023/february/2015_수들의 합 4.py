# n과 a[1], a[2] ... a[n] 주어졌을 때, n * (n + 1) / 2 개의 부분합 중 합이 k인 것이 몇 개 있는지

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [0] + list(map(int, input().split()))
prefix_sum = [0] # 누적합

for i in range(1, n + 1):
    prefix_sum.append(prefix_sum[i - 1] + data[i])

print(prefix_sum)

# 모르겠다 난..