#[더 맵게]
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        heapq.heappush(scoville,x + (y*2))
        count += 1       
        
    return count