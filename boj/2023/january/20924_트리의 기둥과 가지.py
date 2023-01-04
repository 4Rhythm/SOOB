# 나무의 기둥 길이, 가장 긴 가지의 길이
# 기가 노드: 루트 노드에서 순회 시작했을 때, 처음으로 자식 노드 2개 이상인 노드 // 리프 노드가 단 1개인 경우 => 리프 노드 = 기가 노드
#                                                                     // 루트 노드가 기가 노드인 경우도 가능
# 기둥 길이 = 루트 노드부터 기가 노드까지 간선 길이 합
# 가지 = 기가 노드부터 임의의 리프 노드까지, 가지 중 가장 긴 길이 찾기

# n, r = map(int, input().split())
#
# graph = [[] for _ in range(n + 1)]
# for _ in range(n - 1):
#     a, b, d = map(int, input().split())
#     graph[a].append((b, d))
#
# giga = r
# root_giga = 0
#
# while True:
#     if len(graph[giga]) > 1:
#         break
#     if len(graph[giga]) == 0:
#         print(giga, root_giga)
#         exit()
#     root_giga += graph[giga][0][1]
#     r = graph[giga][0][0]
#     giga = r
# # print(giga, root_giga)
#
# answer = []
# l = 0
#
# def dfs(node, l):
#     checkList = graph[node]
#     for i in checkList:
#         node = i[0]
#         l += i[1]
#         dfs(node, l)
#         l -= i[1]
#     if len(checkList) == 0:
#         answer.append(l)
#         return
# dfs(giga, l)
#
# max_l = max(answer)
# print(root_giga, max_l)



# 방향을 생각해야 할 듯
# pypy3로 통과
import sys
sys.setrecursionlimit(10**6)

n, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))
# print(graph)

giga = r
root_giga = 0
if len(graph[giga]) == 1: # 정석
    visited = [False for _ in range(n + 1)]
    visited[giga] = True
    root_giga = graph[giga][0][1]
    giga = graph[giga][0][0]

    while True:
        if len(graph[giga]) == 0:
            break
        elif len(graph[giga]) == 2:
            for i in graph[giga]:
                if visited[i[0]] == True:
                    continue
                visited[giga] = True
                root_giga += i[1]
                giga = i[0]
        else:
            break
elif len(graph[giga]) >= 2: # 루트 노드가 기가 노드인 경우
    visited = [False for _ in range(n + 1)]
    visited[giga] = True
else: # 루트 노드가 기가 노드인데 가지가 없는 경우
    print(0, 0)
    exit()

# 가지 길이 구하기
answer = []
l = 0

def dfs(node, l):
    visited[node] = True
    checkList = graph[node]
    count = 0

    for i in checkList:
        node = i[0]
        if visited[node] == True:
            continue
        count += 1
        l += i[1]
        dfs(node, l)
        l -= i[1]

    if count == 0:
        answer.append(l)
        return
dfs(giga, l)

max_l = max(answer)
print(root_giga, max_l)