# 첫 번째 정수 = 트리의 루트 노드
# 다음에 등장하는 연속된 수의 집합 = 루트의 자식 // 첫 번째 수는 항상 루트 노드 + 1 보다 큼
# 그 다음부터는 자식이 없는 노드의 자식이 됨, 노드가 여러 가지면 가장 작은 수를 가지는 노드의 자식
# 집합은 연속하지 않는 곳에서 구문됨

# 사촌 구하기 => 레벨(높이) 구하기

# while True:
#     n, k = map(int, input().split())
#     if n == 0 and k == 0:
#         break
#
#     node = list(map(int, input().split()))
#
    # tree_level = []
    # tree_level.append((node[0], 0))
    #
    # tmp = node[1]
    # level = 1
    # tree_level.append((tmp, level))
    #
    # leaf = 1
    # tmp_leaf = 0
    #
    # for i in range(2, n):
    #     print(leaf, tmp_leaf)
    #     if level == 1:
    #         if tmp + 1 == node[i]:
    #             leaf += 1
    #             tmp = node[i]
    #             tree_level.append((tmp, level))
    #         else:
    #             tmp = node[i]
    #             level += 1
    #             leaf -= 1
    #             tree_level.append((tmp, level))
    #             tmp_leaf += 1
    #     else:
    #         if tmp + 1 == node[i]:
    #             tmp_leaf += 1
    #             tmp = node[i]
    #             tree_level.append((tmp, level))
    #         else:
    #             tmp = node[i]
    #             if leaf > 0:
    #                 leaf -= 1
    #                 tree_level.append((tmp, level))
    #                 tmp_leaf += 1
    #             else:
    #                 leaf = tmp_leaf
    #                 level += 1
    #                 tree_level.append((tmp, level))

    # 출력: [(1, 0), (3, 1), (4, 1), (5, 1), (8, 2), (9, 2), (15, 2), (30, 2), (31, 2), (32, 2)]



# 풀이
from sys import stdin
from collections import defaultdict

while True:
    n, k = map(int, stdin.readline().split())

    if n == 0 and k == 0:
        break

    node = list(map(int, stdin.readline().split()))
    tree = defaultdict(list)

    root_idx = -1
    for i in range(1, n):
        if node[i] - node[i - 1] > 1:
            root_idx += 1
        tree[node[root_idx]].append(node[i])
        tree[node[i]].append(node[root_idx])
    print(tree)

    # k의 부모, 조상 노드 찾기
    if root_idx == -1:
        print(0)
        continue

    k_par = tree[k][0] # k의 부모
    if k_par > k:
        print(0)
        continue
    k_anc = tree[k_par][0] # k의 조상
    if k_anc > k_par:
        print(0)
        continue

    # k 부모를 제외한 손자들 계산
    cousin = 0
    for par in tree[k_anc]: # k의 조상의 자식들 = k보다 한 세대 위
        if par < k_anc or par == k_par: # 부모 라인의 한 세대 위 또는 k의 부모 제외
            continue
        cousin += len(tree[par][1:])

    print(cousin)