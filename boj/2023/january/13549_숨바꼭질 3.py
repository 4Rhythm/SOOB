# x-1 또는 x+1로 이동 => 1초 소요
# 2x => 0초 소요
# 가장 빠른 시간을 구하기 위해서는 최대한 순간이동(2x, 0초 소요)을 많이 활용해야 함 (...?)
# 노노 그냥 bfs를 사용하는 문제
from collections import deque

def bfs(n, visited):
    queue = deque()
    visited[n] = 1
    queue.append((n, 0))

    while queue:
        now, time = queue.popleft()

        if now == k:
            print(time)
            return
        else:
            if now * 2 <= 100000 and not visited[now * 2]:
                queue.appendleft((now * 2, time))
                visited[2 * now] = 1
            if now + 1 <= 100000 and not visited[now + 1]:
                queue.append((now + 1, time + 1))
                visited[now + 1] = 1
            if 0 <= now - 1 and not visited[now - 1]:
                queue.append((now - 1, time + 1))
                visited[now - 1] = 1

n, k = map(int, input().split())
visited = [0] * 100001
bfs(n, visited)