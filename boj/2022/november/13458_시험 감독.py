# n개 시험장, i번 시험장 응시자 수는 Ai
# 감독관: 총감독관 / 부감독관
# 총감독관 - 응시자 B명, 부감독관 - 응시자 C명
# 한 시험장에 총감독관은 오직 1명, 부감독관은 상관 X

# 필요한 감독관 수의 최솟값 구하기

n = int(input())
test_place = list(map(int, input().split()))
b, c = map(int, input().split())

count = 0

for i in test_place:
    if i > b:
        i = i - b
        count += 1
        if i > c:
            if i % c != 0:
                count += int(i / c) + 1
            else:
                count += int(i / c)
        else:
            count += 1
    else:
        count += 1

print(count)


