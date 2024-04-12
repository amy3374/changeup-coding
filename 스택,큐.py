#[같은 숫자는 싫어]
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])
    return answer


# [기능개발]
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()
    for i in range(len(progresses)):
        x = (100-progresses[i])/speeds[i]
        if x == int(x):
            days.append(int(x))
        else:
            days.append(int(x)+1)
        
    while days:
        count = 1
        temp = days.popleft()
        while days and temp >= days[0]:
            days.popleft()
            count += 1
        answer.append(count)

    return answer


#올바른 괄호
def solution(s):
    answer = 0
    for c in s:
        if c == "(":
            answer += 1
        else:
            if answer > 0:
                answer -= 1
            else:
                return False
    if answer > 0:
        return False
    return True

# 내가 쓴 코드 => 정답이긴 하지만...
# def solution(s):
#     answer = True
#     count = 0
#     temp = []
#     for i in range(len(s)):
#         if s[i] == "(":
#             count += 1
#             temp.append(s[i])
#         if s[i] == ")":
#             count -= 1
#             temp.append(s[i])
#         if count == 0:
#             if temp[0] ==")" or temp[-1] == "(" :
#                 print(temp)
#                 return False
#     if count != 0:
#             return False
    
#     return True



# [프로세스]
from collections import deque

def solution(priorities, location):
    answer = [] # 실행된 프로세스
    queue = deque((i, j) for i, j in enumerate(priorities))
    while queue:
        process = queue.popleft()
        # 우선순위가 더 높은 프로세스가 하나라도 있으면 큐에 다시 추가 / 아니면 해당 프로세스 실행
        if queue and any(process[1] < q[1] for q in queue):
        # if process != max(queue):
            queue.append(process)
        else:
            answer.append(process)
    
    # location 실행 순서 찾기
    for i in answer:
        if i[0] == location:
            return answer.index(i)+1

