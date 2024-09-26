# 도시의 도로는 깊이가 K인 완전 이진 트리
# 깊이가 K인 완전 이진 트리는 총 2K-1개의 노드
# 각 노드에는 그 곳에 위치한 빌딩의 번호
# 가장 마지막 레벨을 제외한 모든 집은 왼쪽 자식과 오른쪽 자식을 가짐

# 상근이는 도시에 있는 모든 빌딩에 들어갔고, 들어간 순서대로 번호를 종이에 적어 놓음
# 한국으로 돌아온 상근이는 도시가 어떻게 생겼는지 그림을 그려보려고 함
# 어떤 순서로 도시를 방문했는지 기억함

# 가장 처음에 상근이는 트리의 루트에 있는 빌딩 앞에 서있음
# 현재 빌딩의 왼쪽 자식에 있는 빌딩에 아직 들어가지 않았다면, 왼쪽 자식으로 이동함
# 현재 있는 노드가 왼쪽 자식을 가지고 있지 않거나 왼쪽 자식에 있는 빌딩을 이미 들어갔다면, 현재 노드에 있는 빌딩을 들어가고 종이에 번호를 적음
# 현재 빌딩을 이미 들어갔다 온 상태이고, 오른쪽 자식을 가지고 있는 경우에는 오른쪽 자식으로 이동함
# 현재 빌딩과 왼쪽, 오른쪽 자식에 있는 빌딩을 모두 방문했다면, 부모 노드로 이동함

# 상근이가 종이에 적은 순서가 모두 주어졌을 때, 각 레벨에 있는 빌딩의 번호를 구하는 프로그램 작성하기

k = int(input())
building = list(map(int, input().split()))
l = len(building)
level_list = [[] for _ in range(k)]

def checkLevel(start, end, level):
    if start == end:
        level_list[level].append(building[start])
        return
    else:
        mid = int((start + end) / 2)
        level_list[level].append(building[mid])

        checkLevel(start, mid - 1, level + 1)
        checkLevel(mid + 1, end, level + 1)


checkLevel(0, l - 1, 0)
for i in level_list:
    print(*i)