n, m = map(int, input().split())
g1 = list(map(str, input()))
g2 = list(map(str, input()))
t = int(input())

g1.reverse()

move = g1 + g2
l = len(move)

for _ in range(t):
    i = 0
    while i < l - 1:
        if move[i] in g1 and move[i + 1] in g2:
            move[i], move[i + 1] = move[i + 1], move[i]
            i += 2
        else:
            i += 1

move = ''.join(map(str, move))

print(move)