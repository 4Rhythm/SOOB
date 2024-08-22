# 영선이는 매우 기쁘기 때문에, 효빈이에게 스마일 이모티콘을 S개 보내려고 함

# 영선이는 이미 화면에 이모티콘 1개를 입력함
# 이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 함

# 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장함
# 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 함
# 3. 화면에 있는 이모티콘 중 하나를 삭제함

# 모든 연산은 1초 걸림

# 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 됨
# 클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없음
# 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없음

# 화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가됨

# 영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값 구하기

# 입력
# 첫째 줄에 S (2 ≤ S ≤ 1000) 가 주어짐
# 출력
# 첫째 줄에 이모티콘을 S개 만들기 위해 필요한 시간의 최솟값 출력

from collections import deque

S = int(input())
screen = 1
copy_now = 0
time = 0

visited = [[False for _ in range(S + 1)] for _ in range(S + 1)]
visited[screen][copy_now] = True

queue = deque([[screen, copy_now, time]])

while queue:
    node = queue.popleft()
    # print('node: ', node)
    screen, copy_now, time = node[0], node[1], node[2]

    if screen == S:
        print(time)
        break

    if 0 <= screen < S + 1 and 0 <= copy_now < S + 1:
        tmp_time = time + 1
        # 1. 화면 복사
        copy_now1 = screen
        if not visited[screen][copy_now1]:
            visited[screen][copy_now1] = True
            queue.append([screen, copy_now1, tmp_time])

        # 2. 화면에 붙여 넣기
        if copy_now > 0 and screen + copy_now <= S:
            screen2 = screen + copy_now
            if not visited[screen2][copy_now]:
                visited[screen2][copy_now] = True
                queue.append([screen2, copy_now, tmp_time])

        # 3. 화면 삭제(-1)
        if screen > 0:
            screen3 = screen - 1
            if not visited[screen3][copy_now]:
                visited[screen3][copy_now] = True
                queue.append([screen3, copy_now, tmp_time])