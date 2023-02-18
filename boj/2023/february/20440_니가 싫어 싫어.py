# 모기들의 방 입장, 퇴장 시간 주어졌을 때 가장 많이 있는 시간대와 해당 시간대에 몇 마리 있는지 구하기

# 풀이 참고
# 리스트를 사용하지말고 딕셔너리를 사용하자 // collection 라이브러리의 defaultdict
# 입장 +1, 퇴장 -1
# 좌표 압축! = 중요한 구간이나 숫자만 가지고 있는 기법
# https://dalseoin.tistory.com/entry/%EB%B0%B1%EC%A4%8020440-%EB%8B%88%EA%B0%80-%EC%8B%AB%EC%96%B4-2

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
dict = defaultdict(int)

for i in range(n):
    e, x = map(int, input().split())
    dict[e] += 1
    dict[x] -= 1

time = sorted(dict.keys())
max_time = [0, 0]# 모기가 가장 많은 시간대
max_cnt = 0 # 가장 많을 때 마리 수
cnt = 0
curr_cnt, next_cnt = 0, 0
flag = False

for i in time: # 모기가 등장하는 시간들
    next_cnt = curr_cnt + dict[i]

    if next_cnt > max_cnt:
        max_cnt = next_cnt
        max_time[0] = i # 시작 시간
        flag = True
    elif next_cnt == max_cnt and flag == True:
        max_time[1] = i # 끝 시간 갱신
    elif next_cnt < max_cnt and flag == True:
        max_time[1] = i
        flag = False
    curr_cnt = next_cnt

print(max_cnt)
print(*max_time)