# [완전탐색 - 카펫]
# 정확성은 ok, but 효율성 문제
def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    for i in range(1, sum+1):
        if sum % i == 0:
            answer.append((i, int(sum//i)))
    return answer[len(answer)//2]

# 검색한 풀이


def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    for b in range(1, sum+1):
        if sum % b == 0:
            a = sum//b
            if a >= b:
                if 2*a + 2*b - 4 == brown:
                    return [a, b]
    return answer
