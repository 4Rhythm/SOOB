# 오늘부터 N+1일째 되는 날 퇴사
# 하루에 하나씩 서로 다른 사람의 상담
# 최대 수익 구하기

n = int(input())

time = [0 for _ in range(n)]
price = [0 for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(n):
    time[i], price[i] = map(int, input().split())

for i in range(n - 1, -1, -1): # 역순으로
    if time[i] + i <= n: # 날짜를 초과하지 않는 경우
        dp[i] = max(dp[i + 1], price[i] + dp[i + time[i]]) # 만약 i가 6이고 time[6]이 2이며, n이 8일 때 => dp[6]은 dp[8] + price[6]과 dp[7]중 큰 값으로 할당
                                                           # 전자는 당일(6일)과 8일에 일한 경우, 후자는 당일(6일)은 일 안하고 다음 날(7일)에 일 할 경우
    else: # 날짜를 초과하는 경우
        dp[i] = dp[i + 1]
print(dp[0])