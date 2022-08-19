# room[i][j]
# 1. 한 쪽 => room[i][j] room[i][j]
# 2. 양 쪽
# 3. 직각
# 4. ㅗ 3방향
# 5. 4방향
#
# 6. 벽!
#
# CCTV는 회전 가능
# CCTV끼리는 통과 O, 벽 통과 X
# 감시 가능 영역 = '#'
# 감시 못하는 영역 = 사각지대
#
# 사각 지대의 최소 크기를 구하라 = 최대한 많이 감시하게끔 CCTV 배치
# 5 ~ 1 순서로 최대값 구하고 배치하기
#
# def first():
#
# # 사무실 세로, 가로
# n, m = map(int, input().split())
# room = []
# for i in range(n):
#     data = list(map(int, input().split()))
#     room.append(data)
#
# for i in room:
#     for j in i:
#
# print(room)