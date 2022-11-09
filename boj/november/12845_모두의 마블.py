# 순서 매겨진 여러 장의 카드, 카드는 각각 레벨이 있음
#
# 카드 A에 카드 B 덧붙이기
# 1. 인접한 카드여야 함
# 2. 업그레이드 된 카드 A의 레벨은 변하지 않음
#
# 카드 합성할 때마다 두 카드 레벨의 합만큼 골드 받음
# 최대 골드는?

# 풀이 참고
n = int(input())
cards = list(map(int, input().split()))
gold = 0

max_gold = 0
idx = 0

for i in range(n):
    if max_gold < cards[i]:
        max_gold = cards[i]
        idx = i

for i in range(n):
    if i == idx:
        continue
    gold += cards[i]

gold += max_gold * (n - 1)

print(gold)