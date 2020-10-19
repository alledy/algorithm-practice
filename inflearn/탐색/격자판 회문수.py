def isPalindrome(arr):
    # arr 5자리
    for i in range(5//2):
        if arr[i] != arr[4-i]:
            return False
    return True

def solution(arr):
    # arr 7*7
    answer = 0
    for i in range(7):
        for j in range(3):
            if isPalindrome(arr[i][j:j+5]):
                answer += 1
            
            my_list = [arr[k][i] for k in range(j,j+5)]
            if isPalindrome(my_list):
                answer += 1

    return answer