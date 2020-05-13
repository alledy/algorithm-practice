class Solution:
    def isAnagram(self, str1, str2, memo):
        if str1 not in memo:
            a1 = [0] * 26
            for x in str1:
                a1[ord(x)-97] += 1
            memo[str1] = a1

        if str2 not in memo:
            a2 = [0] * 26
            for x in str2:
                a2[ord(x)-97] += 1
            memo[str2] = a2

        if memo[str1] == memo[str2]:
            return True
        return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = [[strs[0]]]
        memo = {}
        for i in range(1, len(strs)):
            grouped = False
            for arr in l:
                if self.isAnagram(arr[0], strs[i], memo) is True:
                    arr += [strs[i]]
                    grouped = True
                    break
            if grouped is False:
                l.append([strs[i]])
        return l
