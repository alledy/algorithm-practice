class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R, L, count = 0, 0, 0
        for i in s:
            if i is "R":
                R += 1
            if i is "L":
                L += 1
            if R and R == L:
                count += 1 
                R,L = 0,0
        return count        
                
        
        