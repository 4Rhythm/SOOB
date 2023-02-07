# n명의 원생들을 키 순으로 줄 세움
# 총 k개의 조로 나누려 함
# 한 조에는 원생이 적어도 1명 있어야함

# 풀이참고
# n명을 k개의 그룹으로 나눈다 => n - k개의 키 차이를 무시할 수 있다는 뜻
# 차이를 저장하고 가장 큰 차이 k - 1개를 뺀 나머지 합
n, k = map(int, input().split())
person = list(map(int, input().split()))

diff = []
for i in range(n - 1):
    diff.append(person[i + 1] - person[i])
diff.sort()

answer = 0
for i in range(n - k):
    answer += diff[i]
print(answer)