'''Runtime

15 ms | Beats 44.57%

Memory

19.50 MB | Beats 30.32%'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts,countt={},{}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i],0)
            countt[t[i]] = 1 + countt.get(t[i],0)
        for j in counts:
            if counts[j] != countt.get(j,0):
                return False
        return True