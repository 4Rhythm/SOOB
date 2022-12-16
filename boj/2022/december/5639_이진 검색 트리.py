# 이진 검색 트리
# 왼쪽 서브 트리에 있는 모든 노드의 키는 노드의 키보다 작음
# 오른쪽 서브 트리에 있는 모든 노드의 키는 노드의 키보다 큼

# 왼쪽, 오른쪽 서브 트리도 이진 검색 트리임

# 전위 순회한 결과 주어지면, 후위 순회한 결과를 구하라

# 전위 순회 결과를 통해 원래의 그래프를 구하자..

# 루트 -> 왼 -> 오

# 다음 노드가 작다면, 왼쪽 노드, 크다면 오른쪽 노드

# level = 0
# root = -1
# before = -1
# graph = []
#
#
# while True:
#     node = int(input())
#
#     if root == -1:
#         root = node
#         before = node
#         graph[root] = []
#         # level += 1
#         continue
#
#     if before > node:
#         graph[before][0] = node
#     else:



# 풀이 참고
import sys

sys.setrecursionlimit(10 ** 6)
nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break

def postorder(first, end):
    if first > end:
        return
    mid = end + 1  # 오른쪽 노드가 없을 경우

    for i in range(first + 1, end + 1):
        if nums[first] < nums[i]:
            mid = i
            break

    postorder(first + 1, mid - 1)  # 왼쪽 확인
    postorder(mid, end)  # 오른쪽 확인
    print(nums[first])

postorder(0, len(nums) - 1)


