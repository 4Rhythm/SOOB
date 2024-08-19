# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파됨
# 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 됨

# 어느 날 1번 컴퓨터가 웜 바이러스에 걸림
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수 출력

# 입력
# 첫째 줄에는 컴퓨터의 수가 주어짐
# 컴퓨터의 수는 100 이하인 양의 정수
# 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨짐
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어짐
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어짐

# 출력
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력

from collections import deque

computers = int(input())
edges = int(input())

graph = [[] for _ in range(computers + 1)]
visited = [False for _ in range(computers + 1)]
visited[1] = True
answer = 0

for _ in range(edges):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque(graph[1])

while queue:
    computer = queue.popleft()
    if not visited[computer]:
        answer += 1
        visited[computer] = True
        for c in graph[computer]:
            queue.append(c)

print(answer)


