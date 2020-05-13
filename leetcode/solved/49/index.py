class Solution:
    def convert(self, s):
        a = [0] * 26
        for x in s:
            a[ord(x)-97] += 1
        return ''.join([str(x) for x in a])

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = self.convert(s)
            d[key] = d.get(key, []) + [s]
        return d.values()
