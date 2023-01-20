# 영수 => 1 ~ 9 서로 다른 숫자 3자리 수 생각함
# 민혁 => 1 ~ 9 서로 다른 숫자 3자리 수 물어봄
# 동일한 자리 = 스트라이크, 다른 자리 = 볼
# 가능성 있는 수 총 몇 개인지
import itertools

n = int(input())
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

answer = list(itertools.permutations(num, 3))
for _ in range(n):
    q, s, b = map(int, input().split())
    remove = 0
    q = list(str(q))

    for i in range(len(answer)):
        s_count, b_count = 0, 0
        i -= remove
        for j in range(3):
            if answer[i][j] == q[j]: # 스트라이크
                s_count += 1
            elif q[j] in answer[i]:  # 볼
                b_count += 1

        if (s != s_count) or (b != b_count):
            answer.remove(answer[i])
            remove += 1

print(len(answer))

