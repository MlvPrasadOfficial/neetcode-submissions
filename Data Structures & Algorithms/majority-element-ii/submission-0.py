class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        ct = defaultdict(int)
        for i in nums :
            ct[i] += 1        
        res = []
        for j in ct :
            if ct[j] > (len(nums)/3) :
                res.append(j)
        return res        