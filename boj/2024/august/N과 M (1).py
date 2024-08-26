# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기
# 조건: 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# 입력
# 첫째 줄에 자연수 N과 M이 주어짐 (1 ≤ M ≤ N ≤ 8)

# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력
# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 함

# 수열은 사전 순으로 증가하는 순서로 출력해야 함

from itertools import permutations

N, M = map(int, input().split())

numbers = []
for i in range(1, N + 1):
    numbers.append(i)

answer = list(permutations(numbers, M))
for ans in answer:
    print(" ".join(map(str, ans)))
