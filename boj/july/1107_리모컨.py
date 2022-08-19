# 일부 숫자 버튼 고장남
# 0 ~ 9, +, -
# 0에서 - 누른 경우 변하지 않음

# 현재 100번, 이동하려는 채널 n
# n으로 이동하기 위해서 버튼 최소 몇 번 눌러야 하는지

# 1. 숫자를 눌러서 채널 이동
# 2. +, - 버튼 눌러서 채널 이동

# "이동하려는 채널"과 "숫자 눌러서 이동할 수 있는 채널"의 차를 절댓값으로 계산해서 가장 작은 수 구하기
# 숫자의 자릿수 + 절댓값과 절댓값 중 최소값 리턴

n = int(input())
m = int(input())
if m == 0:
    broke = []
else:
    broke = list(map(int, input().split()))

# 현재 채널
now = 100
# 절댓값 (현재채널과 목표채널)
absValue = abs(n-now)
# 최소 절댓값 변수
minAbs = 9999999
# 가능한 채널들
data = []
# 채널 시작 지점 or 도착 지점 변수
checkpoint = 0

# 가능한 채널들 찾기
def find(x, y):
    if x <= 0:
        x = 0
    for i in range(x, y):
        cnt = 0
        for j in broke:
            if str(j) in str(i):
                break
            else:
                cnt += 1
        if cnt == m:
            data.append(i)
    # print(data)

    for d in data:
        tmp = abs(d - n)
        global minAbs
        minAbs = min(minAbs, tmp + len(str(d)))

    if min(absValue, minAbs) == absValue:
        print(absValue)
        return absValue
    else:
        print(minAbs)
        return minAbs

if now < n:
    checkpoint = n + absValue
    find(now, checkpoint)
elif now > n:
    checkpoint = n - absValue
    find(checkpoint, now)
else:
    print(0)

# data = [1, 2, 3, 4]
# for i in data:
#     if str(i) in "123":
#         print("yes")