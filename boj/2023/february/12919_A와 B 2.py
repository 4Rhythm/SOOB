# S와 T가 주어졌을 때 S를 T로 바꾸는 게임
# 1. 문자열 뒤에 A 추가하기
# 2. 문자열 뒤에 B 추가하고 문자열 뒤집기
# from collections import deque
#
# s = input()
# t = input()
#
# q = deque()
# q.append(s)
#
# l = 0
# target_l = len(t)
#
# while l <= target_l:
#     node = q.popleft()
#     l = len(node)
#
#     node1 = node + 'A'
#
#     node2 = node + 'B'
#     node2 = node2[::-1]
#
#     if t == node1 or t == node2:
#         print(1)
#         exit()
#
#     q.append(node1)
#     q.append(node2)
# print(0)

# 메모리 초과 ㅠㅠ

# 풀이 참고
# s -> t가 아닌 t -> s 가 되는지 확인하자
# t의 마지막에 A가 있으면 제거하고, t의 맨 앞이 B라면 맨 앞의 B를 제외하고, 문자열을 뒤집는 방식
s = list(input())
t = list(input())

def check(t):
    if t == s:
        print(1)
        exit()

    if len(t) == 0:
        return

    if t[-1] == 'A':  # 마지막이 A인 경우
        check(t[:-1])  # A 제거 후 재귀호출

    if t[0] == 'B':  # 처음이 B인 경우
        check(t[1:][::-1])  # B 제거 후, 뒤집어서 재귀호출

check(t)
print(0)