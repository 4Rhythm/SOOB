n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visited = [False] * n
answer = []

def back(depth, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    prev = 0
    for i in range(n):
        if not visited[i] and prev != num[i]:
            visited[i] = True
            answer.append(num[i])
            prev = num[i]
            back(depth + 1, n, m)
            visited[i] = False
            answer.pop()

back(0, n, m)