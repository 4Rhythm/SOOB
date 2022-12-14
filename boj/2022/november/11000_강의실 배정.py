# Si에서 시작해서 Ti에 끝나는 N개의 수업
# 최소의 강의실을 사용하여 모든 수업 가능하게 해야 함

# (수업이 끝난 직후에 다음 수업을 시작할 수 있음)

# n = int(input())
# class_time = []
#
# for _ in range(n):
#     s, t = map(int, input().split())
#     class_time.append((s, t))
# # print(class_time)
#
# class_time = sorted(class_time, key=lambda x: (x[0], x[1]))
# print(class_time)
# 정렬까진 했는데..

# 풀이 참고하여 진행, 우선순위 큐(힙 큐) 자료구조 사용하기!
import heapq

n = int(input())
class_time = []

for _ in range(n):
    s, t = map(int, input().split())
    class_time.append([s, t])
# print(class_time)

# class_time = sorted(class_time, key=lambda x: (x[0], x[1]))
class_time.sort()
# print(class_time)

room = []
heapq.heappush(room, class_time[0][1])

for i in range(1, n):
    if class_time[i][0] < room[0]:
        heapq.heappush(room, class_time[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, class_time[i][1])
print(len(room))

