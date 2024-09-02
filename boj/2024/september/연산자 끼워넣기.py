# N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어짐
# 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어짐
# 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있음

# 우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있음
# 이때, 주어진 수의 순서를 바꾸면 안 됨

# 예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고,
# 주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있음

# 1+2+3-4×5÷6
# 1÷2+3+4-5×6
# 1+2÷3×4-5+6
# 1÷2×3-4+5+6

# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 함
# 나눗셈은 정수 나눗셈으로 몫만 취함
# 음수를 양수로 나눌 때는 C++14의 기준을 따름 => 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같음

# 1+2+3-4×5÷6 = 1
# 1÷2+3+4-5×6 = 12
# 1+2÷3×4-5+6 = 5
# 1÷2×3-4+5+6 = 7

# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하기

# 입력
# 첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어짐
# 둘째 줄에는 A1, A2, ..., AN이 주어짐 (1 ≤ Ai ≤ 100)
# 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수

# 출력
# 첫째 줄에 만들 수 있는 식의 결과의 최댓값 출력
# 둘째 줄에는 최솟값 출력한다.
#
# 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어짐
# 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같음

from collections import defaultdict

N = int(input())
numbers = list(map(int, input().split()))
sign_count = list(map(int, input().split()))
global max_value
global min_value
max_value = -1000000001
min_value = 1000000001
now_value = numbers[0]
idx = 1

sign = defaultdict(int)
sign['+'] += sign_count[0]
sign['-'] += sign_count[1]
sign['*'] += sign_count[2]
sign['/'] += sign_count[3]

def back(sign, idx, now_value):
    global max_value
    global min_value

    if idx == N:
        max_value = max(max_value, now_value)
        min_value = min(min_value, now_value)
        return

    tmp_value = now_value

    for k, v in sign.items():
        if v > 0:
            if k == '+':
                tmp_value += numbers[idx]
            elif k == '-':
                tmp_value -= numbers[idx]
            elif k == '*':
                tmp_value *= numbers[idx]
            else:
                if tmp_value < 0:
                    tmp_value = -(-tmp_value // numbers[idx])
                else:
                    tmp_value = tmp_value // numbers[idx]

            sign[k] -= 1
            idx += 1
            back(sign, idx, tmp_value)
            tmp_value = now_value
            sign[k] += 1
            idx -= 1

back(sign, idx, now_value)

print(max_value)
print(min_value)