# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 오름차순
# 조건을 만족하는 길이가 M인 수열 구하기
from itertools import combinations

n, m = map(int, input().split())
num = []
for i in range(1, n + 1):
  num.append(i)

answer = list(combinations(num, m))

for i in answer:
  tmp = " ".join(map(str, i))
  print(tmp)