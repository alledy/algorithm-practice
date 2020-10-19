"""
문제
앞으로 읽으나 뒤로 읽으나 같은 문자열 -> 회문 문자열
이면 YES 출력, 아니면 NO 출력
대소문자 구분하지 않음
""" 

# lowercase 

def isPalindrome(s):
    s = s.lower()
    if len(s) == 1:
        return True
    if len(s) == 2:
        if s[0] == s[1]:
            return True    
    if s[0] != s[-1]:
        return False
    if isPalindrome(s[1:-1]):
        return True
    
    """
    문자열이 두 글자일 때 앞글자와 뒷글자를 떼는 케이스는 생각하지 않는게 좋겠다
    """

    ### 
    
    def isPalindrome2(s):
        s = s.lower()
        for i in range(len(s)//2):
            if s[i] != s[-1-s]:
                return False
        else:
            return True 