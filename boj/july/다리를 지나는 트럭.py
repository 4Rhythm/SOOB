# 다리에 올라갈 수 있는 트럭, 다리의 길이: bridge_length
# 다리가 견딜 수 있는 무게: weight 이하
#
# 최소 몇 초?

from collections import deque

def solution(bridge_length, weight, truck_weights):

    count = 0

    truck = deque(truck_weights)
    bridge = deque()
    total = 0 # 다리 위 트럭 수

    for i in range(bridge_length):
        bridge.append(0)

    while True:
        # 대기 트럭이 있다면,
        if len(truck) != 0:
            count += 1

            # 다리 위 트럭과 다음 대기 트럭의 무게 합이 weight 보다 작고(현재 다리 위 트럭 무게 합이 weight 보다도 작을테니), 다리 위 트럭 수가 bridge_length 보다 작다면,
            if sum(bridge) + truck[0] <= weight and total < bridge_length:
                bridge.append(truck.popleft())
                total += 1
            else:
                bridge.append(0)
            tmp = bridge.popleft()
            if tmp != 0:
                if sum(bridge) == 0:
                    total -= 1
                    count -= 1
            print(bridge)

        else:
            while sum(bridge) != 0:
                bridge.append(0)
                bridge.popleft()
                count += 1


            print(bridge)
            return count
# 1, 4, 6, 8 ~ 13 실패, 5 시간초과