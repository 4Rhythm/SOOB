# 자연수는 4개 이하의 제곱수 합으로 표현 가능
import itertools
import math

# n = int(input())
# end = math.floor(math.sqrt(n))
#
# numbers = []
# for i in range(1, end + 1):
#     cnt = i**2
#     if cnt == n:
#         print(1)
#         exit()
#     numbers.append(cnt)
# # print(numbers) # [1, 4, 9, 16, 25]
#
# for i in range(1, 4):
#     answer_list = []
#     tmp = list(itertools.combinations(numbers, i))
#
#     for j in tmp:
#         answer_list.append(sum(j))
#     answer_list.sort()
#
#     for a in answer_list:
#         if n == a:
#             print(i)
#             exit()
#         if n < a:
#             break
# print(4)


n = int(input())

if int(math.sqrt(n)) == math.sqrt(n):
    print(1)
    exit()

for i in range(1, int(math.sqrt(n)) + 1):
    if int(math.sqrt(n - (i ** 2))) == math.sqrt(n - (i ** 2)):
        print(2)
        exit()

for i in range(1, int(math.sqrt(n)) + 1):
    for j in range(1, int(math.sqrt(n - i ** 2)) + 1):
        if int(math.sqrt(n - (i ** 2) - (j ** 2))) == math.sqrt(n - (i ** 2) - (j ** 2)):
            print(3)
            exit()
print(4)