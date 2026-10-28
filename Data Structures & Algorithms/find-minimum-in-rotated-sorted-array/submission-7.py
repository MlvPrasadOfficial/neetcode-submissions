class Solution:
    def findMin(self, nums: List[int]) -> int:

        i = 0 
        j = len(nums) - 1
        if nums[i] < nums[j] or j == 0 :
                return nums[i]
        mn = nums[j] # 2
        while i <  j : # 3 5
            print(i,j) # 0 5 - 3 2
            mid = (i + j)//2 # 4 - 1
            if j - i == 1 or i == j :
                return min(nums[j],nums[i])
            if nums[mid] <  nums[j] : # 6 > 5
                j = mid # 3
                mn = nums[mid]
            elif  nums[mid] > nums[j] :
                i = mid
                
            


        
        