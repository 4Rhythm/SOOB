# N개의 자연수 중 M개를 고른 수열
# 사전순
# 조건을 만족하는 길이가 M인 수열 구하기

# 백트래킹
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
answer = []

def back(idx):
  if len(answer) == m:
    print(" ".join(map(str, answer)))
    return

  for i in range(idx, n):
      answer.append(num[i])
      back(i)
      answer.pop()

idx = 0
back(0)