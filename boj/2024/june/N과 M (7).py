# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기
# N개의 자연수는 모두 다른 수

# 조건 1: N개의 자연수 중에서 M개를 고른 수열
# 조건 2: 같은 수를 여러 번 골라도 됨

# 첫째 줄에 N과 M (1 ≤ M ≤ N ≤ 7)
# 둘째 줄에 N개의 수
# 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수

from itertools import product

N, M = map(int, input().split())
tmp_nums = list(map(int, input().split()))
tmp_nums.sort()

nums = product(tmp_nums, repeat=M)

for num in nums:
    answer = ' '.join(map(str, list(num)))
    print(answer)
