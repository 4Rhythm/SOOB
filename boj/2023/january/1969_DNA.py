from collections import Counter

n, m = map(int, input().split())

graph = [[] for _ in range(m)]
dna_list = []
dna = ''

for _ in range(n):
    tmp = input()
    dna_list.append(tmp)
# print(dna_list) # ['ATGTTACCAT', 'AAGTTACGAT', 'AACAAAGCAA', 'AAGTTACCTT', 'AAGTTACCAA', 'TACTTACCAA']

for i in dna_list:
    for j in range(m):
        graph[j].append(i[j])
# print(graph) # [['A', 'A', 'A', 'A', 'A', 'T'], ['T', 'A', 'A', 'A', 'A', 'A'], ['G', 'G', 'C', 'G', 'G', 'C'], ['T', 'T', 'A', 'T', 'T', 'T'], ['T', 'T', 'A', 'T', 'T', 'T'], ['A', 'A', 'A', 'A', 'A', 'A'], ['C', 'C', 'G', 'C', 'C', 'C'], ['C', 'G', 'C', 'C', 'C', 'C'], ['A', 'A', 'A', 'T', 'A', 'A'], ['T', 'T', 'A', 'T', 'A', 'A']]

for i in graph:
    tmp_counter = Counter(i)
    sort_tmp_counter = sorted(tmp_counter.items(), key=lambda x: (-x[1], x[0])) # value값 내림차순, key값 오름차순
    # print(sort_tmp_counter) # [('T', 4), ('A', 1)]  ....  [('C', 4), ('T', 1)]
    dna += sort_tmp_counter[0][0]
print(dna)

hd = 0
for d in dna_list:
    for i in range(m):
        if d[i] != dna[i]:
            hd += 1
print(hd)