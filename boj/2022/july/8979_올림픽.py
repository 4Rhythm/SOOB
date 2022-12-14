# 우선순위
# 1. 금메달
# 2. 금메달 같으면 은메달
# 3. 금, 은 같으면 동메달
# + (모두 같으면 같은 등수)
#
# 한 국가의 등수 = 자신보다 더 잘한 나라 수 + 1
# => 자신보다 잘한 나라의 수를 구하면 됨

n, k = map(int, input().split())
count = 0
score = []

for _ in range(n):
    s = list(map(int, input().split()))
    score.append(s)
    if s[0] == k:
        k_score = s

for i in score:
    if i[1] > k_score[1]:
        count += 1
    elif i[1] == k_score[1]:
        if i[2] > k_score[2]:
            count += 1
        elif i[2] == k_score[2]:
            if i[3] > k_score[3]:
                count += 1

print(count + 1)
