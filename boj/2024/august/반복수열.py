# D[1] = A
# D[n] = D[n-1]의 각 자리의 숫자를 P번 곱한 수들의 합
# 예를 들어 A=57, P=2일 때, 수열 D는 [57, 74(=52+72=25+49), 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37, …]이 됨
# 그 뒤에는 앞서 나온 수들(57부터가 아니라 58부터)이 반복됨

# 이와 같은 수열을 계속 구하다 보면 언젠가 이와 같은 반복수열이 됨
# 반복되는 부분을 제외했을 때, 수열에 남게 되는 수들의 개수를 구하가


# 첫째 줄에 A(1 ≤ A ≤ 9999), P(1 ≤ P ≤ 5)가 주어짐
# 반복되는 부분을 제외했을 때, 수열에 남게 되는 수들의 개수를 출력

A, P = map(int, input().split())
D = [A]
dict = {A: 1}
num = 0
answer = 0

while True:
    tmp_A = 0

    str_num = str(D[num])

    for i in range(0, len(str_num)):
        tmp_A += int(str_num[i]) ** P

    if tmp_A not in dict:
        dict[tmp_A] = 1
    else:
        if dict[tmp_A] == 2:
            break
        else:
            dict[tmp_A] += 1

    D.append(tmp_A)
    num += 1

for k, v in dict.items():
    if v == 1:
        answer += 1

print(answer)

