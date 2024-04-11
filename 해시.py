#[폰켄몬]
def solution(nums):
    unique = list(set(nums))
    nums_length = int(len(nums)/2)
    
    if len(unique) > nums_length:
        return nums_length
    else:
        return len(unique)
    

#[전화번호 목록]
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
            return False
        
    return True
# def solution(phone_book):
    # phone_book.sort()
    # for i in range(len(phone_book) - 1):
    #     if phone_book[i+1].startswith(phone_book[i]):
    #         return False
    # return True