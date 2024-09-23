# 최소 스패닝 트리 템플릿
# import sys
#
# n, m = map(int, sys.stdin.readline().rstrip().split())
#
# parent = [i for i in range(n + 1)]
#
# def get_parent(x):
#     if parent[x] == x:
#         return x
#     parent[x] = get_parent(parent[x]) # get_parent 거슬러 올라가면서 parent[x] 값도 갱신
#     return parent[x]
#
# def union_parent(a, b):
#     a = get_parent(a)
#     b = get_parent(b)
#
#     if a < b: # 작은 쪽이 부모가 됨 (한 집합 관계 => 부모가 따로 있는 건 아님)
#         parent[b] = a
#     else:
#         parent[a] = b
#
# def same_parent(a, b):
#     return get_parent(a) == get_parent(b)


# 모든 건물이 도로를 통해 연결되도록 최소한의 도로 만들기

# 입력
# 첫 번째 줄에 건물의 개수 N, 도로의 개수 M
# 두 번째 줄 부터 M + 1줄까지 건물의 번호 a, b와 두 건물 사이 도로를 만들 때 드는 비용 c
# 같은 쌍의 건물을 연결하는 두 도로는 주어지지 않음

# 출력
# 예산을 얼마나 절약 할 수 있는지 출력함
# 만약 모든 건물이 연결되어 있지 않는다면 -1 출력

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

road = []
total = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    road.append((a, b, c))
    total += c
road.sort(key=lambda x: x[2])

# Union-Find
parent = [i for i in range(N + 1)]

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])

    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a, b):
    return find_parent(a) == find_parent(b)

for a, b, cost in road:
    if not same_parent(a, b):
        union_parent(a, b)
        total -= cost

count = 0
for i in range(1, N):
    if i == parent[i]:
        count += 1

if count > 1:
    print(-1)
else:
    print(total)