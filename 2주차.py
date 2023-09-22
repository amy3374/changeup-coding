# [그리디 - 큰 수 만들기 --> 시간초과 실패]
from itertools import combinations


def solution(number, k):
    answer = list(combinations(number, len(number) - k))
    result = []
    # print(answer)
    for i in answer:
        result.append(int(''.join(i)))
    return str(max(result))

# [정렬 - 가장 큰 수 --> 실패]


def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)
    for i in numbers:
        answer += i
    # print(numbers)
    return answer
