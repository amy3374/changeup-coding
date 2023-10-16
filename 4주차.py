# [깊이/너비 우선탐색(DFS/BFS) - 단어변환]
def bfs(begin, target, words):

    queue = deque()
    queue.append([begin, 0])

    while queue:
        now, cnt = queue.popleft()

        if now == target:
            return cnt

        for word in words:
            temp_cnt = 0
            for i in range(len(now)):  # 단어의 길이만큼 반복하여
                if now[i] != word[i]:  # 단어에 알파벳 한개씩 체크하기
                    temp_cnt += 1

            if temp_cnt == 1:
                queue.append([word, cnt+1])

# [그리디 - 단어변환]


def solution(people, limit):
    people.sort()
    answer = 0
    start = 0
    end = len(people) - 1  # 시작과 끝 지정
    while start <= end:
        # 최소 + 최대로 2명 태울 수 있는 경우
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
            answer += 1
        else:
            end -= 1
            answer += 1
    return answer
