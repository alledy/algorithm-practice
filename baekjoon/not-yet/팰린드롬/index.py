import sys
sys.setrecursionlimit(10000)
with open('10942.txt', 'r') as sys.stdin:

    total_n = sys.stdin.readline()
    str_list = sys.stdin.readline().split()
    total_q = input()
    
    memo = {}

    def getKey(list):
        return "s".join(list)

    def isPalindrome(memo, seq):
        if len(seq) == 1:
            return 1

        if len(seq) == 2:
            return 1 if seq[0] == seq[1] else 0
        
        key = getKey(seq)
        
        if key in memo:
            return memo[key]
        else:
            memo[key] = 1 if (seq[0] == seq[-1]) and (isPalindrome(memo, seq[1:-1]) == 1) else 0

        return memo[key]

    for i in range(total_q):
        temp = sys.stdin.readline().split()
        start = int(temp[0])-1
        end = int(temp[1])
        check_seq = str_list[start:end]
        print(isPalindrome(memo, check_seq))
