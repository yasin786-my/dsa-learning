'''Runtime
7
ms
Beats
57.36%
Memory
21.28
MB
Beats
18.58%'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count,res = 0,0
        for n in nums:
            if count == 0:
                res = n
            count += ( 1 if n == res else -1) 
        return res