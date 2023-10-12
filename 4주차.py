
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
