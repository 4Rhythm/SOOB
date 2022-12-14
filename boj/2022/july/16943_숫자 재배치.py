# a와 b
# a에 포함된 숫자의 순서를 섞어 새로운 수 c
# c < b 조건 만족하는 가장 큰 값, 가능한 c 없으면 -1 출력
# c는 0으로 시작 X

import itertools

a, b = map(int, input().split())

a = list(map(int, str(a))) # 1234 => [1, 2, 3, 4]
a_len = len(a)
data = list(itertools.permutations(a)) # [1, 2, 3, 4] => [(1, 2, 3, 4), (1, 2, 4, 3), ... , (4, 3, 2, 1)]

values = []
for i in data:
    value = ''.join(map(str, i))
    values.append(value)

values = list(map(int, values))
# print(values)

# 최대값
maxValue = -1

for i in values:
    # b보다 작고 숫자의 길이가 a의 길이와 같은 경우 (맨 앞에 0이 오는 경우는 a의 길이와 다름)
    if i < b and len(str(i)) == a_len:
        maxValue = max(maxValue, i)

print(maxValue)