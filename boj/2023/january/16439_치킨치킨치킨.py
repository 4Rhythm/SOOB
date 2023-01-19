# N명의 회원, M 종류 치킨
# 회원마다 선호도 존재, 한 사람의 만족도는 선호도 중 가장 큰 값으로 결정됨
# 회원들의 만족도 합이 최대가 되도록 주문하기
# 최대 3가지 종류의 치킨만 시키기
import itertools

n, m = map(int, input().split())
like = []
check_index = []

# 선호도 초기화
for i in range(n):
    tmp = list(map(int, input().split()))
    like.append(tmp)
# print(like) # [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 2, 1]]

# 체크할 인덱스 리스트 초기화
for i in range(m):
    check_index.append(i)
# print(check_index) # [0, 1, 2, 3, 4]

check_list = list(itertools.combinations(check_index, 3))
# print(check_list) # [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

answer = []

for i in check_list:
    tmp = 0
    for j in like:
        tmp += max(j[i[0]], j[i[1]], j[i[2]])
    answer.append(tmp)
# print(answer) # [11, 11, 12, 12, 13, 12, 11, 12, 11, 11]

print(max(answer))



