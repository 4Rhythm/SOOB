# 1부터 N까지 자연수 중에서 중복 허용하여 M개를 고른 수열
# 사전순
# 조건을 만족하는 길이가 M인 수열 구하기

# 백트래킹
n, m = map(int, input().split())
answer = []

def back(x):
  if len(answer) == m:
    print(" ".join(map(str, answer)))
    return

  for i in range(x, n + 1):
    answer.append(i)
    back(i)
    answer.pop()
back(1)