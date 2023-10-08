# [해시 - 의상]
from itertools import permutations


def solution(clothes):
    hash_map = {}
    for cloth, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1

    answer = 1
    for type in hash_map:
        answer *= (hash_map[type] + 1)

    return answer - 1


# [완전탐색 - 피로도]


def solution(k, dungeons):
    answer = 0

    for p in permutations(dungeons, len(dungeons)):
        piro = k
        count = 0

        for x, y in p:
            if piro >= x:
                piro -= y
                count += 1
        answer = max(answer, count)
    return answer
