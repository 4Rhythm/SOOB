# 미국 전역의 나무들이 주어졌을 때, 각 종이 전체에서 몇 %를 차지하는지 구하기

# 입력
# 프로그램은 여러 줄로 이루어져 있으며, 한 줄에 하나의 나무 종 이름이 주어짐
# 어떤 종 이름도 30글자를 넘지 않으며, 입력에는 최대 10,000개의 종이 주어지고 최대 1,000,000그루의 나무가 주어짐

# 출력
# 주어진 각 종의 이름을 사전순으로 출력하고, 그 종이 차지하는 비율을 백분율로 소수점 4째자리까지 반올림해 함께 출력함

# Red Alder
# Ash
# Aspen
# Basswood
# Ash
# Beech
# Yellow Birch
# Ash
# Cherry
# Cottonwood
# Ash
# Cypress
# Red Elm
# Gum
# Hackberry
# White Oak
# Hickory
# Pecan
# Hard Maple
# White Oak
# Soft Maple
# Red Oak
# Red Oak
# White Oak
# Poplan
# Sassafras
# Sycamore
# Black Walnut
# Willow

import sys

dic = {}
total = 0

while True:
    tree = sys.stdin.readline().rstrip()
    if tree == '':
        break

    if tree in dic.keys():
        dic[tree] += 1
    else:
        dic[tree] = 1
    total += 1

sorted_dict = sorted(dic.items(), key=lambda item: item[0])

for key, value in sorted_dict:
    rate = (value / total) * 100

    print("%s %.4f" %(key, rate))


    # per = (a / total * 100)
    #
    # print("%s %.4f" %(i, per))