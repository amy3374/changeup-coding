#[k번째 수]
def solution(array, commands):
    answer = []
    temp=[]
    for i in commands:
        for j in array:
            temp = array[i[0]-1:i[1]]
        temp.sort()
        answer.append(temp[i[2]-1])
            
        
    return answer


#[가장 큰 수]
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: str(x)*3, reverse = True)
#     answer=''
#     for i in numbers:
#         answer += str(i)
    
#     return str(int(answer))
    return str(int(''.join(numbers)))