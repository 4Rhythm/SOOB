from itertools import combinations

N, M = map(int, input().split())

numbers = []
for i in range(1, N + 1):
    numbers.append(i)

comb = list(combinations(numbers, M))

for c in comb:
    for d in c:
        print(d, end=' ')
    print()


