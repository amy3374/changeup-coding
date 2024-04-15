#[게임맵 최단거리]
from collections import deque
def solution(maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    answer = 0
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]):
                    continue
                if maps[nx][ny]==0:
                    continue
                if maps[nx][ny]==1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny))
        if maps[len(maps)-1][len(maps[0])-1] == 1:
            return -1
        else:
            return maps[len(maps)-1][len(maps[0])-1]
    answer = bfs(0,0)
    return answer


#[타겟넘버]
def solution(numbers, target):
    leaves = [0]
    count = 0
    
    for num in numbers:
        temp = []
        for leaf in leaves:
            temp.append(leaf+num)
            temp.append(leaf-num)
        leaves = temp
    
    for leaf in leaves:
        if leaf == target:
            count += 1
    return count

#[네트워크]
from collections import deque
    
def solution(n, computers):
    answer = 0
    queue = deque()
    
             
    def bfs(i):
        queue.append(i)
        while queue:
            i = queue.popleft()
            visited[i] = 1
            for a in range(n):
                if computers[i][a] and not visited[a]:
                    queue.append(a)
                    
    visited = [0 for i in range(len(computers))]

    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
        
    return answer