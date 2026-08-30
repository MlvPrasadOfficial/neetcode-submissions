class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0 
        j = 1
        ct = 1

        while j < len(nums) :

            if nums[i] == nums[j] :
                j = j + 1
            else :
                nums[i+1] = nums[j]
                i = i + 1
                j  = j + 1
                ct += 1

        return ct
        # 1 1 2 3 4

        # i = 2
        # j = 3
