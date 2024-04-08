# [카펫]
def solution(brown, yellow):
    answer = []
    width = 0
    height = 0
    total = brown+yellow
    for i in range(1,total):
        if total % i == 0:
            width = total//i
            height = i
            if width >= height and (width-2)*(height-2)==yellow:
                return [width,height]
    
    return answer

#[피로도]


from itertools import permutations

def solution(k,dungeons):
    answer = 0
    for p in permutations(dungeons,len(dungeons)):
        piro = k
        count = 0
        print(p)
        for i in range(len(p)):
            if piro >= p[i][0]:
                count += 1
                piro -= p[i][1]
            
        answer = max(answer,count)

    return answer


#[소수찾기]
from itertools import permutations

def is_sosu(x):
    if x < 2:
        return False
    
    for i in range(2,x):
        if x%i == 0:
            return False
    return True
    
def solution(numbers):
    answer = 0
    
    num = []
    for i in range(1, len(numbers)+1) :
        num.extend(list(set(map(''.join,permutations(numbers, i)))))
        temp = list(set(map(int,num)))

    for t in temp:
        if is_sosu(t) == True:
            answer += 1
        
    return answer

#[모의고사]
def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    answer=[]
    scores = [0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == first[i%5]:
            scores[0] += 1
        if answers[i] == second[i%8]:
            scores[1] += 1
        if answers[i] == third[i%10]:
            scores[2] += 1
        
    for i in range(len(scores)):
        if scores[i] == max(scores):
            answer.append(i+1)
                
    return answer


#[최소 직사각형]
def solution(sizes):
    answer = 0
    x = 0
    y = 0
    for size in sizes:
        size.sort()
        x = max(x,size[0])
        y = max(y,size[1])
        
    return int(x*y)