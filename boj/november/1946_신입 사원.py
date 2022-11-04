# 1차 2차 점수 모두 다른 사람보다 떨어지면 탈락
#
# 한 명을 확인할 때 그 사람보다 1차 순위가 높은 사람 중 2차 순위도 높은 사람을 체크하기

# 1차 시간초과..
# t = int(input())
# answer = []
# for _ in range(t):
#     count = 0
#     n = int(input())
#     new_employee = []
#
#     for _ in range(n):
#         em = list(map(int, input().split()))
#         new_employee.append(em)
#
#     for em in new_employee:
#         tmp = 0
#         checkFirst = em[0]
#         checkSecond = em[1]
#         for em in new_employee:
#             if checkFirst == em[0]:
#                 continue
#             if checkFirst > em[0]:
#                 if checkSecond > em[1]:
#                     tmp = 1
#                     break
#         if tmp == 0:
#             count += 1
#     answer.append(count)
#
# for a in answer:
#     print(a)



# 풀이 참고
from sys import stdin
input = stdin.readline

t = int(input())
answer = []

for _ in range(t):
    count = 0
    n = int(input())
    new_employee = []

    for _ in range(n):
        em = list(map(int, input().split()))
        new_employee.append(em)

    new_employee.sort(key=lambda x: x[0])

    count += 1
    top = new_employee[0][1]

    for i in range(1, n):
        if top > new_employee[i][1]:
            top = new_employee[i][1]
            count += 1

    answer.append(count)

for a in answer:
    print(a)






