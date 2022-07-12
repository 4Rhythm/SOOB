# 지도 N * N, 각 칸에는 높이
# 길 = 한 행, 한 열 전부 // 한족 끝에서 다른쪽 끝까지
# 길 지나려면 모든 칸의 높이가 모두 같아야 됨 // 경사로 높이 1, 길이 L
# 다음칸이 같은지, 낮은지, 높은지 체크

# 결론 = h h h h // h-1 L개 + h 1개

n, l = map(int, input().split())
data = []
answer = 0

for _ in range(n):
    line = list(map(int, input().split()))
    data.append(line)

# 한 행에서의 길
for i in data:
    j = 0
    base = 0 # 경사로 놓을 수 있는 칸 (l과 같아야 놓을 수 있음)
    h = 0 # 높이 기록용 변수
    route = True
    while j < n:
        if j == n - 1:
            break

        # 다음 칸도 높이 같은 경우
        if i[j] == i[j + 1]:
            j += 1
            base += 1

        # 다음 칸의 높이가 다른 경우
        else:
            base += 1
            # 다음 칸의 높이가 +1인 경우
            if i[j] + 1 == i[j + 1]:
                if base >= l:
                    j += 1
                else:
                    route = False
                    base = 0
                    break
            # 다음 칸의 높이가 -1인 경우
            elif i[j] - 1 == i[j + 1]:
                h = i[j]
                check = 0
                # 다음 오는 l개의 칸 높이가 h - 1인지 check
                for k in range(j+1, l+1):
                    if h - 1 == i[k]:
                        check += 1
                    else:
                        break
                # 만약 h 다음 (h - 1)이 l개라면,
                if check == l:
                    j += l
                else:
                    base = 0
                    route = False
                    break
            # 다음 칸의 높이 차가 |2| 이상인 경우
            else:
                base = 0
                route = False
                break

    if route == True:
        answer += 1

# 행과 열을 바꿔준 swap_data
swap_data = []
for i in range(n):
    sd = []
    for j in range(n):
        sd.append(data[j][i])
    swap_data.append(sd)

# 한 열에서의 길
for i in swap_data:
    j = 0
    base = 0 # 경사로 놓을 수 있는 칸 (l과 같아야 놓을 수 있음)
    h = 0 # 높이 기록용 변수
    route = True
    while j < n:
        if j == n - 1:
            break

        # 다음 칸도 높이 같은 경우
        if i[j] == i[j + 1]:
            j += 1
            base += 1

        # 다음 칸의 높이가 다른 경우
        else:
            base += 1
            # 다음 칸의 높이가 +1인 경우
            if i[j] + 1 == i[j + 1]:
                if base >= l:
                    j += 1
                else:
                    route = False
                    base = 0
                    break
            # 다음 칸의 높이가 -1인 경우
            elif i[j] - 1 == i[j + 1]:
                h = i[j]
                check = 0
                # 다음 오는 l개의 칸 높이가 h - 1인지 check
                k = 0
                for k in range(j+1, l+1):
                    if h - 1 == i[k]:
                        check += 1
                    else:
                        break
                # 만약 h 다음 (h - 1)이 l개라면,
                if check == l:
                    j += l
                    base = 0
                else:
                    base = 0
                    route = False
                    break
            # 다음 칸의 높이 차가 |2| 이상인 경우
            else:
                base = 0
                route = False
                break

    if route == True:
        answer += 1

print(answer)