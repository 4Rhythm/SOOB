k = int(input())
building = list(map(int, input().split()))
l = len(building)
level_list = [[] for _ in range(k)]

def checkLevel(start, end, level):
    if start == end:
        level_list[level].append(building[start])
        return
    else:
        mid = int((start + end) / 2)
        level_list[level].append(building[mid])

        checkLevel(start, mid - 1, level + 1)
        checkLevel(mid + 1, end, level + 1)

checkLevel(0, l - 1, 0)
for i in level_list:
    print(*i)