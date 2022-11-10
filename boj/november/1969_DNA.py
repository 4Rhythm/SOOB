n, m = map(int, input().split())
dna_list = [] # dna 모음
dna_place_list = [[] for _ in range(m)] # dna의 각 자리 글자 모음
answer = []
hd = 0

for i in range(n):
    dna = input()
    dna_list.append(dna)
    for j in range(m):
        dna_place_list[j].append(dna[j])
# print(dna_list)
# print(dna_place_list)

for i in dna_place_list:
    i.sort()
    tmp = max(i, key=i.count) # 리스트에서 빈도수가 가장 높은 요소 찾기
    answer.append(tmp)
s = ''.join(map(str, answer))
print(s)

for i in dna_list:
    for j in range(m):
        if i[j] != s[j]:
            hd += 1
print(hd)
