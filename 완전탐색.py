# [완전탐색 - 카펫]
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