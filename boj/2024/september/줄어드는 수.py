# 음이 아닌 정수를 십진법으로 표기했을 때, 왼쪽에서부터 자리수가 감소할 때, 그 수를 줄어드는 수라고 함
# 예를 들어, 321와 950은 줄어드는 수이고, 322와 958은 아님

# N번째로 작은 줄어드는 수를 출력하는 프로그램
# 만약 그러한 수가 없을 때는 -1을 출력
# 가장 작은 줄어드는 수가 1번째 작은 줄어드는 수

# 입력
# N이 주어짐
# N은 1,000,000보다 작거나 같은 자연수

# 출력
# 첫째 줄에 N번째 작은 줄어드는 수를 출력

N = int(input())
result = set()
numbers = []

def back():
    if numbers:
        result.add(int(''.join(map(str, numbers))))

    for i in range(0, 10):
        if len(numbers) == 0 or numbers[-1] > i:
            numbers.append(i)
            back()
            numbers.pop()

back()
result = sorted(result)

if len(result) >= N:
    print(result[N - 1])
else:
    print(-1)