from itertools import permutations

N, M = map(int, input().split())

numbers = []
for i in range(1, N + 1):
    numbers.append(i)

perm = list(permutations(numbers, M))

for p in perm:
    for k in p:
        print(k, end=' ')
    print()


