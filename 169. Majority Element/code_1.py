"""Runtime
21
ms
Beats
6.61%
Memory
21.10
MB
Beats
46.98%"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        maxCount,res = 0,0
        for n in nums:
            count[n] = 1+ count.get(n,0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n],maxCount)
        return res