# [프로그래머스-완전탐색-소수찾기]
from itertools import permutations


def is_prime_number(x):
    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0

    num = []
    for i in range(1, len(numbers)+1):
        num.extend(list(set(map(''.join, permutations(numbers, i)))))
    per = list(set(map(int, num)))
    print(num)
    print(per)

    for p in per:
        if is_prime_number(p) == True:
            answer += 1

    return answer

# [프로그래머스-깊이/너비 우선 탐색(DFS/BFS)-타겟넘버]


def solution(numbers, target):
    leaves = [0]
    count = 0

    for num in numbers:
        temp = []
        # 자손 노드
        for leaf in leaves:
            temp.append(leaf + num)
            temp.append(leaf - num)

        leaves = temp
        # print(leaves)

    for leaf in leaves:
        if leaf == target:
            count += 1

    return count

# [프로그래머스-연습문제-공원산책]


def solution(park, routes):
    x = 0
    y = 0

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = j
                y = i
                break

    for route in routes:
        new_x = x
        new_y = y
        for r in range(int(route[2])):
            if route[0] == 'E' and new_x < len(park[0])-1 and park[new_y][new_x+1] != 'X':
                new_x += 1
