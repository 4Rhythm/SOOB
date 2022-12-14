#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

# 맨 위에서 보면, 1 -> 1, 2
# 그 다음 층은, 1 -> 1, 2  // 2 -> 2, 3
# 그 다음 층은, 1 -> 1, 2  // 2 -> 2, 3 // 3 -> 3, 4

# 항상 선택지가 "두 개"이며, 자기 자신과 같은 인덱스, 자기 자신 + 1 인덱스 인 것을 알 수 있음
# 최대 합을 구해야 하므로, 맨 위층부터 층 단위로 차근차근 값을 저장해가며 내려가면 될 듯

# 예외 있음
# 1층에서 2층은 괜찮은데.. 그 뒤로 내려가면 가운데 값들이 각각 두 개가 됨, 최댓값을 할당해줘야 함
# 양 끝이 아니라면 비교를 통해 값 하나를 정해야 함

# deque를 이용해서 해당 원소를 pop, 다음층의 선택지 2개와 연산하여 다시 append

from collections import deque
n = int(input())
triangle = []

for _ in range(n):
    data = list(map(int, input().split()))
    triangle.append(data)

# print(triangle)

# 각 층에 도달했을 때의 누적 합들
answer = deque()

# 초기화 (맨 윗층)
answer.append(triangle[0][0])

def solution(answer, i):
    count = i   # triangle의 몇 번째 층인지
    tmp = 0

    tmp_deque = deque()

    for j in range(count):
        pick = answer.popleft()

        one = pick + triangle[count][tmp]
        two = pick + triangle[count][tmp + 1]

        if count == 1:
            answer.append(one)
            answer.append(two)
        else:
            tmp_deque.append(one)
            tmp_deque.append(two)

        tmp += 1

    check = len(tmp_deque)
    if check != 0:
        answer.append(tmp_deque.popleft())
        for k in range(int((check - 2) / 2)):
            o = tmp_deque.popleft()
            t = tmp_deque.popleft()
            if o >= t:
                answer.append(o)
            else:
                answer.append(t)
        answer.append(tmp_deque.popleft())

    # print(i, "층: 함수 끝")
    # print(answer)

for i in range(1, n):
    solution(answer, i)
# print(answer)

print(max(answer))