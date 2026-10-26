class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # class Solution:
    # def search(self, nums: List[int], target: int) -> int:
        t = target
        i = 0 
        j = len(nums) - 1

        # if 

        if nums[i] >= target :
            return 0
        if nums[j] < target :
            return j + 1

        

        while i < j :
            print("1")
            
            if nums[i] == target :
                # return 3
                return i
            if nums[j] == target :
                return j
            m = (i + j )//2 
            if m == i or m == j  :
                return m + 1 
            if nums[m] == t : 
                return m 
            if t < nums[m] :
                j = m
            if t > nums[m] :
                i = m


        return -1 