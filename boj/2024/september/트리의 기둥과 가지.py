# 나무의 기둥의 길이와 가장 긴 가지의 길이 구하기

# "기가 노드"는 루트 노드에서 순회를 시작했을 때, 처음으로 자식 노드가 2개 이상인 노드
# 기둥-가지를 줄여 기가 노드

# 단, 리프 노드가 단 1개인 경우 리프 노드가 동시에 기가 노드
# 루트 노드가 동시에 기가 노드인 경우도 가능

# 트리의 기둥: 루트 노드에서부터 기가 노드까지
# 기둥의 길이: 기둥의 간선 길이의 합

# 트리의 가지: 기가 노드에서부터 임의의 리프 노드까지
# 가지의 길이: 가지의 간선 길이의 합

# 트리의 기둥과 가장 긴 가지의 길이 구하기

n, r = map(int, input().split())  # 노드 개수, 루트 노드 번호

pillar, branch = 0, 0
giga = 0
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def find_giga_pillar(node, pillar):
    visited[node] = True

    cnt = 0
    tmp_pillar = 0
    next_node = 0

    for tmp_node in graph[node]:
        n = tmp_node[0]
        if not visited[n]:
            cnt += 1
            next_node = n
            tmp_pillar += tmp_node[1]

    if cnt > 1:  # 기가노드
        return [node, pillar]
    elif cnt == 0:  # 기가노드이면서 리프노드
        pillar += tmp_pillar
        return [node, pillar]
    else:  # 노드
        pillar += tmp_pillar
        return find_giga_pillar(next_node, pillar)

result = find_giga_pillar(r, 0)
giga, pillar = result[0], result[1]

max_length = 0


def find_max_branch(giga, l):
    global max_length  # 가장 긴 거리를 저장할 전역 변수

    if l > max_length:
        max_length = l

    for neighbor in graph[giga]:
        tmp_node = neighbor[0]
        tmp_dist = neighbor[1]

        if not visited[tmp_node]:
            visited[tmp_node] = True
            # 연결된 노드로 이동하며 거리 증가
            find_max_branch(tmp_node, l + tmp_dist)

    return max_length

max_l = find_max_branch(giga, 0)

print(pillar, max_l)
