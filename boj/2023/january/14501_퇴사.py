# n = int(input())
# data = []
# for _ in range(n):
#     t, p = map(int, input().split())
#     data.append((t, p))
#
# answer = []
#
# def find(day, profit):
#
#     tmp_t = data[day][0]
#     tmp_p = data[day][1]
#
#     if day + tmp_t < n:
#         find(day + tmp_t, profit + tmp_p)
#     else:
#         answer.append(profit)
#         return
#
#     if day + 1 < n:
#         find(day + 1, profit)
#     else:
#         answer.append(profit)
#         return
#
# find(0, 0)
# print(max(answer))



n = int(input())
data = []
for _ in range(n):
    t, p = map(int, input().split())
    data.append((t, p))
answer = 0

def find(day, profit):
    global answer

    if day == n:
        answer = max(answer, profit)
        return

    tmp_t = data[day][0]
    tmp_p = data[day][1]

    if day + tmp_t <= n:
        find(day + tmp_t, profit + tmp_p)

    find(day + 1, profit)

for day in range(n):
    find(day, 0)
print(answer)