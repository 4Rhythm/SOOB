# 단절점: 정점 제거하였을 때, 그 정점이 포함된 그래프가 2개 이상으로 나뉘는 경우 => 정점 = 단절점
# 단절선: 간선 제거하였을 때, 그 간선이 포함된 그래프가 2개 이상으로 나뉘는 경우 => 간선 = 단절선

# 트리: 사이클 존재 X, 모든 정점이 연결되어 있음

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if len(graph[k]) > 1:
            print("yes")
        else:
            print("no")
    else:
        print("yes")



# 풀이 참고, 연결 관계가 아닌 연결된 갯수만 체크
import sys

input = sys.stdin.readline

n = int(input())
graph = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a] += 1
    graph[b] += 1

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if graph[k] > 1:
            print("yes")
        else:
            print("no")
    else:
        print("yes")