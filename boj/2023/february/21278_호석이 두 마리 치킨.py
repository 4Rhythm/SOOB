# 도시 안에 2개의 매장
# n개의 건물과 m개의 도로
# 건물 1번부터 n번 번호
# i번째 도로는 서로 다른 두 건물 ai번과 bi번 사이를 1시간에 양방향으로 이동할 수 있는 도로
#
# 도시에서 2개의 건물 골라 치킨집
# 건물 x의 접근성은 x에서 가장 가까운 치킨집까지 왕복하는 최단 시간
#
# 모든 건물에서 가장 가까운 치킨집까지 왕복하는 최단시간의 총합을 최소화할 수 있는 건물 2개 고르기
# 이런 건물 조합 여러 개라면, 건물 번호 중 작은 번호는 더 작게, 같다면 큰 번호가 더 작을수록 좋음

# n, m = map(int, input().split())
#
# graph = [[-1] * (n + 1) for _ in range(n + 1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1

# 풀이 참고
# 플로이드 워셜 O(N^3) // 모든 정점에서 모든 정점으로 가는 최소 거리 구하기 ⇒ 플로이드 와샬
# 1. M개 만큼 a와 b를 입력받고 a와 b사이의 거리를 1로 cost 배열에 넣어준다.
# 2. 플로이드-와샬 알고리즘을 통해 각 건물 사이의 거리를 구해준다.
# 3. 브루트포스 방식으로 치킨집이 1번, 2번일 때 부터 1번, 3번 ... N-1번, N번 까지일 때 모든 도시에서의 왕복 시간의 합을 비교하며 최솟값을 찾아서 출력한다.

n, m = map(int, input().split())  # 건물 n, 도로 m
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(n):
    graph[k][k] = 0
    for i in range(n + 1):
        for j in range(n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

max = INF
for i in range(1, n):
    for j in range(2, n + 1):
        sum = 0
        for k in range(1, n + 1):
            sum += min(graph[k][i], graph[k][j]) * 2
        if max > sum:
            max = sum
            answer = [i, j, max]
print(*answer)






