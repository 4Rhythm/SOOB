a = int(input())
t = int(input())
q = int(input()) # 0: 뻔, 1: 데기

graph = []
b, dg = 0, 0
turn = 1
person = 0

check = ''
if q == 0:
    check = 'b'
else:
    check = 'dg'

while True:
    for i in range(2):
        b += 1
        graph.append(('b', b, person % a))
        person += 1
        dg += 1
        graph.append(('dg', dg, person % a))
        person += 1

    for i in range(turn + 1):
        b += 1
        graph.append(('b', b, person % a))
        person += 1

    for i in range(turn + 1):
        dg += 1
        graph.append(('dg', dg, person % a))
        person += 1

    if t <= b:
        break

    turn += 1

for g in graph:
    if g[1] == t:
        if check == g[0]:
            print(g[2])
            break