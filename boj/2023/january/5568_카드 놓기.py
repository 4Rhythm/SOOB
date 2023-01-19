# 카드 n장 (4 ~ 10장)
# 각 카드에는 1 ~ 99 정수, 이 중 k(2 ~ 4)장 선택하고 가로로 정수 만들기
# 만들 수 있는 정수는 몇 가지?
import itertools

n = int(input())
k = int(input())
card = []

for i in range(n):
    tmp = input()
    card.append(tmp)
# print(card) # ['1', '2', '12', '1']

case = set(list(itertools.permutations(card, k))) # 중복 제거
# print(case) # {('1', '2'), ('2', '12'), ('12', '1'), ('12', '2'), ('2', '1'), ('1', '12'), ('1', '1')}

check_case = []
for c in case:
    tmp = ''.join(map(str, c))
    check_case.append(tmp)
# print(check_case) # ['21', '12', '212', '112', '11', '122', '121']
check_case = set(check_case) # 중복 제거

print(len(check_case))