# k개 로프, 중량 w 물체
# k개 로프를 사용하여 중량 w

# 풀이참고)
# 작은 중량을 드는 로프가 최대 무게를 결정함을 알 수 있음
# => 최소 중량을 드는 로프 * 연결하는 로프의 수 = 최대 중량

n = int(input())
rope = []
result = []

for _ in range(n):
    tmp = int(input())
    rope.append(tmp)

rope.sort(reverse=True)

for i in range(len(rope)):
    tmp = (i + 1) * rope[i]
    result.append(tmp)

print(max(result))