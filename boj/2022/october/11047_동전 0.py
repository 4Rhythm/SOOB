# 동전 N종류
# 합 K
# 필요한 동전 개수 최솟값

n, k = map(int, input().split())
coins = []

for _ in range(n):
    coin = int(input())
    coins.append(coin)

answer = 0

while len(coins) != 0:
    c = coins.pop()
    if k // c > 0:
        answer += k // c
        k = k % c
    else:
        continue

print(answer)