# 출발: 상근이네 집, 도착: 펜타포트 락 페스티벌
# 맥주 한 박스 = 맥주 20개
# 50미터 당 1병

# 편의점: 빈 병 버리고 새 맥주

# 도착 가능하면 happy, 아니면 sad 출력

from collections import deque

def bfs():
    queue = deque()
    queue.append([home[0], home[1]])

    while queue:
        x, y = queue.popleft()

        if abs(festival[0] - x) + abs(festival[1] - y) <= 1000:
            print("happy")
            return

        for i in range(n):
            if not visited[i]:
                nx, ny = store[i][0], store[i][1]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    queue.append([nx, ny])
                    visited[i] = 1
    print("sad")
    return

t = int(input())

for i in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    store = []
    if n == 0:
        pass
    else:
        for _ in range(n):
            tmp = list(map(int, input().split()))
            store.append(tmp)
    festival = list(map(int, input().split()))
    visited = [0 for i in range(n + 1)]
    bfs()