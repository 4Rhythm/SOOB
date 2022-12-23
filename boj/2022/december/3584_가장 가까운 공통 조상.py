# 루트가 있는 트리, 그 트리 상의 두 정점이 주어지면 가장 가까운 공통 조상을 찾기
# A, B => A가 B의 부모
# 아이디어: 조상을 찾아야하므로 거꾸로 그래프 그려보기

case = int(input())

for _ in range(case):
  n = int(input())
  graph = [[] for _ in range(n + 1)]
  for l in range(n - 1):
    a, b = map(int, input().split())

    graph[b].append(a)

  # print(graph)
  find_a, find_b = map(int, input().split())
  find_A = [find_a]
  find_B = [find_b]

  while True:
    if not graph[find_a]:
      break
    find_A.append(graph[find_a][0])
    find_a = graph[find_a][0]

  while True:
    if not graph[find_b]:
      break
    find_B.append(graph[find_b][0])
    find_b = graph[find_b][0]

  for i in find_A:
    cnt = 0
    for j in find_B:
      if i == j:
        cnt = 1
        print(j)
        break
    if cnt == 1:
      break