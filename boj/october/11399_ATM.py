# atm 1대, n명
n = int(input())
p = list(map(int, input().split()))
p.sort()

add = 0
answer = 0

for i in p:
    add += i
    answer += add

print(answer)