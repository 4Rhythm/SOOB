# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 조건을 만족하는 길이가 M인 수열 구하기
from itertools import permutations

n, m = map(int, input().split())
num = []
for i in range(1, n + 1):
  num.append(i)

answer = list(permutations(num, m))

for i in answer:
  tmp = " ".join(map(str, i))
  print(tmp)



# 백트래킹 풀이 참조
n, m = map(int, input().split())
answer = []

def back():
  # 배열의 길이를 확인, 재귀 탈출 조건
  if len(answer) == m:
    print(" ".join(map(str, answer)))
    return
    # 1 ~ N 까지
  for i in range(1, n + 1):
    # 중복 확인
    if i not in answer:
      # 배열 추가
      answer.append(i)
      # 재귀
      back()
      # return으로 돌아오면 이게 실행됨
      # 1, 2, 3 일때 3을 없앰으로 전 단계로 돌아가는 것
      answer.pop()
  print(answer)
back()