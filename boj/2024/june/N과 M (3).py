from itertools import product

N, M = map(int, input().split())

numbers = []
for i in range(1, N + 1):
    numbers.append(i)

prod = list(product(numbers, repeat=M))

for p in prod:
    for k in p:
        print(k, end=' ')
    print()