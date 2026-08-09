'''Runtime

20 ms | Beats 6.18%

Memory

20.22 MB | Beats 18.60%'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)