# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기

# 조건 1: N개의 자연수 중에서 M개를 고른 수열
# 조건 2: 같은 수를 여러 번 골라도 됨
# 조건 3: 고른 수열은 비내림차순이어야 함

# 첫째 줄에 N과 M (1 ≤ M ≤ N ≤ 8)
# 둘째 줄에 N개의 수
# 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수

# 한 줄에 하나씩 문제의 조건을 만족하는 수열 출력
# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 함
# 수열은 사전 순으로 증가하는 순서로 출력해야 함

def choose(x):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return

    prev = 0

    for i in range(x, N):
        if prev != nums[i]:
            answer.append(nums[i])
            prev = nums[i]
            choose(i)
            answer.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

answer = []

choose(0)