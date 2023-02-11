# 화물을 배에 실어야 함
# 크레인 n대, 1분에 박스 하나씩
# 모든 크레인은 동시에 움직임
#
# 각 크레인은 무게 제한이 있음
# from collections import deque

n = int(input())
crane = list(map(int, input().split()))
crane.sort(reverse=True)

m = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)
# box = deque(box)

answer = 0

if box[0] > crane[0]:
    print(-1)
    exit()

# while len(box) != 0:
#     for c in crane:
#         for j in range(len(box)):
#             if c >= box[j]:
#                 box.popleft()
#                 break
while box:
    for c in crane:
        for i in range(len(box)):
            if c >= box[i]:
                box.pop(i)
                break
    answer += 1
print(answer)

# 예시
# 3
# 6 8 9
# 6
# 2 4 4 5 9 9
# 답은 3 아닌 2

# 왜 deque는 시간 초과, list는 통과???