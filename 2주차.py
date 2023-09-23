# [그리디 - 큰 수 만들기 --> 시간초과 실패]
from collections import deque
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


# [깊이/넓이 우선탐색(DFS/BFS) - 게임 맵 최단거리]


def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps):
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
        if maps[len(maps)-1][len(maps[0])-1] == 1:
            return -1
        else:
            return maps[len(maps)-1][len(maps[0])-1]
    answer = bfs(0, 0)
    return answer
