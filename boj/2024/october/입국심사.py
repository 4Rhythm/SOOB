# 상근이 + 친구들 = 총 M명
# 입국심사대 = 총 N개
# k번 심사대에 앉아있는 심사관이 한 명을 심사를 하는데 드는 시간은 Tk

# 가장 처음에 모든 심사대는 비어있고, 심사를 할 준비를 모두 끝냈음
# 지금 심사를 기다리고 있는 사람은 모두 상근이와 친구들

# 한 심사대에서는 한 번에 한 사람만 심사를 할 수 있음
# 가장 앞에 서 있는 사람은 비어있는 심사대가 보이면 거기로 가서 심사를 받을 수 있음
# 하지만 항상 이동을 해야 하는 것은 아니다. 더 빠른 심사대의 심사가 끝나길 기다린 다음에 그 곳으로 가서 심사를 받아도 됨

# 상근이와 친구들이 심사를 받는데 걸리는 시간의 최솟값을 구하기

# 입력
# 첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ M ≤ 1,000,000,000)
# 다음 N개 줄에는 각 심사대에서 심사를 하는데 걸리는 시간인 Tk가 주어짐 (1 ≤ Tk ≤ 109)

# 출력
# 첫째 줄에 상근이와 친구들이 심사를 마치는데 걸리는 시간의 최솟값을 출력

def find_min_time(M, times):
    left, right = 1, max(times) * M  # 최소 1초, 최대 심사 시간 * M명
    result = right

    while left <= right:
        mid = (left + right) // 2

        total_people = 0

        # 각 심사대에서 mid 시간 동안 처리할 수 있는 사람 수를 합산
        for time in times:
            total_people += mid // time

            if total_people >= M:
                break

        if total_people >= M:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

N, M = map(int, input().split())
times = []

for _ in range(N):
    time = int(input())
    times.append(time)

print(find_min_time(M, times))