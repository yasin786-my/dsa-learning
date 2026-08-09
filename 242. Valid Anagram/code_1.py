"""Runtime

6 ms | Beats 93.30%

Memory

19.40 MB | Beats 75.92% """
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)