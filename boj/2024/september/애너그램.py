# 애너그램 프로그램
# 입력받은 영단어의 철자들로 만들 수 있는 모든 단어를 출력하는 것
# ex) "abc" 를 입력받았다면, "abc", "acb", "bac", "bca", "cab", "cba" 를 출력해야 함

# 입력받은 단어내에 몇몇 철자가 중복될 수 있음
# 이 경우 같은 단어가 여러 번 만들어 질 수 있는데, 한 번만 출력해야 함
# 또한 출력할 때에 알파벳 순서로 출력해야 함

# 입력
# 첫째 줄에 단어의 개수 N
# 둘째 줄부터 N개의 영단어 (소문자로 이루어져 있음)
# 단어의 길이는 20보다 작거나 같고, 애너그램의 수가 100,000개 이하인 단어만 입력으로 주어짐

# 출력
# 각각의 영단어마다 모든 가능한 애너그램을 출력함
# 각각의 영단어에 대한 애너그램을 출력할 때, 알파벳 순서로 중복되지 않게 출력함

# 2
# abc
# acba

# from itertools import permutations
#
# N = int(input())
# words = []
#
# for _ in range(N):
#     words.append(input())
#
# for w in words:
#     l = len(w)
#     tmp_w = list(w)
#     tmp_data = list(permutations(tmp_w, l))
#
#     result = []
#
#     for d in tmp_data:
#         data = ''.join(d)
#         result.append(data)
#
#     result = list(set(result))
#     result.sort()
#
#     for r in result:
#         print(r)

# import sys
# def back(data, start, end):
#     if start == end:
#         result.append(''.join(data))
#     else:
#         for i in range(start, end):
#             # 요소 교환
#             data[start], data[i] = data[i], data[start]
#             # 다음 위치에 대한 순열 생성
#             back(data, start + 1, end)
#             # 원래 위치로 되돌리기 (백트래킹)
#             data[start], data[i] = data[i], data[start]
#
# N = int(sys.stdin.readline())
# words = []
# visited = [False for _ in range(N)]
#
# for _ in range(N):
#     words.append(input())
#
# for w in words:
#     result = []
#     back(list(w), 0, len(w))
#     result = list(set(result))
#     result.sort()
#     for r in result:
#         print(r)

from collections import defaultdict
import sys

input = sys.stdin.readline

def back(word, length):
    if len(word) == length:
        print("".join(word))
        return

    for a in alphabet:
        if alphabet[a]:
            alphabet[a] -= 1
            back(word + a, length)
            alphabet[a] += 1

N = int(input())

for _ in range(N):
    words = sorted(list(input().strip()))
    alphabet = defaultdict(int)

    for w in words:
        alphabet[w] += 1

    back('', len(words))