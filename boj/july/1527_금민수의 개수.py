# 금민수 = 4와 7로만 이루어진 수
# A보다 크거나 같고 B보다 작거나 같은 자연수 중 금민수의 개수 출력

a, b = map(int, input().split())

num = 0
# 결과
result = 0

def call(num):

    if num > b:
        return

    if (a <= num and num <= b):
        global result
        result += 1

    call(num * 10 + 4)
    call(num * 10 + 7)

call(4)
call(7)
print(result)