# 점화식 = f(n) = f(n-1) + f(n-2) + f(n-3), (n >= 4)

answer = []
t = int(input())

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solution(n - 1) + solution(n - 2) + solution(n - 3)

for _ in range(t):
    n = int(input())
    answer.append(solution(n))

for i in answer:
    print(i)