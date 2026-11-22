class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        seen = [0] * len(nums) 
        for i in nums :
            if seen[i] == -1 :
                return i
            else :
                seen[i] = -1
            
        return -1

        