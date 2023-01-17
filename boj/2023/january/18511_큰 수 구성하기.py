n, k = map(int, input().split())
k_list = list(map(int, input().split()))

answer = n
while True:
    cnt = 0
    for i in str(answer):
        if int(i) not in k_list:
            cnt = 1
            break
    if cnt == 0:
        print(answer)
        break
    answer -= 1