# 알파벳은 열, 숫자는 행
# 열은 왼쪽부터 A ~ H, 숫자는 아래부터 1 ~ 8
from copy import deepcopy

king, rock, n = map(str, input().split())
king = list(king)
rock = list(rock)
n = int(n)
move = []
for _ in range(n):
    m = input()
    move.append(m)

for i in move:
    moveKing = deepcopy(king)
    moveRock = deepcopy(rock)

    if i == "R":
        moveKing[0] = chr(ord(moveKing[0]) + 1)
    elif i == "L":
        moveKing[0] = chr(ord(moveKing[0]) - 1)
    elif i == "B":
        moveKing[1] = int(moveKing[1]) - 1
    elif i == "T":
        moveKing[1] = int(moveKing[1]) + 1
    elif i == "RT":
        moveKing[0] = chr(ord(moveKing[0]) + 1)
        moveKing[1] = int(moveKing[1]) + 1
    elif i == "LT":
        moveKing[0] = chr(ord(moveKing[0]) - 1)
        moveKing[1] = int(moveKing[1]) + 1
    elif i == "RB":
        moveKing[0] = chr(ord(moveKing[0]) + 1)
        moveKing[1] = int(moveKing[1]) - 1
    else:
        moveKing[0] = chr(ord(moveKing[0]) - 1)
        moveKing[1] = int(moveKing[1]) - 1

    if moveKing[0] == moveRock[0] and int(moveKing[1]) == int(moveRock[1]):
        moveRock[0] = chr(ord(rock[0]) + ord(moveKing[0]) - ord(king[0]))
        moveRock[1] = int(rock[1]) + int(moveKing[1]) - int(king[1])

    if ('A' <= moveKing[0] <= 'H') and (1 <= int(moveKing[1]) <= 8) and ('A' <= moveRock[0] <= 'H') and (1 <= int(moveRock[1]) <= 8):
        king[0] = moveKing[0]
        king[1] = moveKing[1]
        rock[0] = moveRock[0]
        rock[1] = moveRock[1]

king = ''.join(map(str, king))
rock = ''.join(map(str, rock))
print(king)
print(rock)