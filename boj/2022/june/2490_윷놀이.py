# 배(0)
# 등(1)

# 도(배1, 등3) => 3 // 개(배2, 등2) => 2 // 걸(배3, 등1) => 1 // 윷(배4) => 0 // 모(배0, 등4) => 4

n = 3
for i in range(n):
    yut = list(map(int, input().split()))
    total = sum(yut)

    if total == 3:
        print('A')
    elif total == 2:
        print('B')
    elif total == 1:
        print('C')
    elif total == 0:
        print('D')
    else:
        print('E')