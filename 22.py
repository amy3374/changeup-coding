T = int(input())
for test_case in range(1, T + 1):
    #######################################################################################################
    N,k= list(map(int,input().split()))
    count = 0
    case = list(map(int,input().split()))
    case.sort()
    for i in range(0,len(case)-1):   
        if case[-1] - case[0] <= k:
            count = len(case)
            break
        if case[i+1]- case[i] <= k:
            count += 1
        else:
            count = 1
    print(count)