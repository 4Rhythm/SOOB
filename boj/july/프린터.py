# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J) 꺼냄
# 2. 나머지 인쇄 대기목록에 J보다 중요도 높은 문서 하나라도 있으면 J를 맨 마지막에 넣기 // 그게 아니면 J 인쇄

from collections import deque

def solution(priorities, location):

    count = 0

    printer = deque(priorities)

    while True:
        j = printer.popleft()

        if len(printer) == 0:
            count += 1
            break

        # 출력하고 싶은 문서의 현재 위치가 0일 때
        if location == 0:
            if j >= max(printer):
                count += 1 # 출력한 문서 횟수 +1
                break
            else:
                printer.append(j)
                location += len(printer) - 1

        # 출력하고 싶은 문서의 현재 위치가 0이 아닐 때 = 다른 문서가 맨 앞에 있을 때
        else:
            location -= 1  # 출력하고 싶은 문서의 위치는 한 칸 앞으로
            if j >= max(printer):
                count += 1 # 출력한 문서 횟수 +1
            else:
                printer.append(j)

    return count



# 예전 내 풀이
def solution(priorities, location):
    answer = 0

    while len(priorities) > 0:
        if priorities[0] >= max(priorities):
            priorities.pop(0)
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
        else:
            priorities.append(priorities[0])
            priorities.pop(0)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer



