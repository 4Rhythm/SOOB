# 원소는 0 ~ 1000 => 한자리 수, 두자리 수, 세자리 수, 네자리 수(는 1000만 가능)

# 풀이
def solution(numbers):
    numbers = list(map(str, numbers)) # str로 변환하여 저장한 이유: 문자열 정렬 순서를 활용하기 위해 // 만약 정렬을 한다면 ['6', '10', '2'] => ['10', '2', '6']
    numbers.sort(key=lambda x: x * 3, reverse=True) # 문자열을 3번 반복한 것을 기준으로 정렬 (1000 이하의 수이므로)

    return str(int(''.join(numbers))) # int -> str 변환 이유: 모든 값이 0인 경우를 처리하기 위해

# 숫자와 문자열 각각 sort 했을 때 비교
# data = [3, 30, 34, 5, 9]
# data.sort()
# print(data) # [3, 5, 9, 30, 34]
#
# data2 = ['3', '30', '34', '5', '9']
# data2.sort()
# print(data2) # ['3', '30', '34', '5', '9']