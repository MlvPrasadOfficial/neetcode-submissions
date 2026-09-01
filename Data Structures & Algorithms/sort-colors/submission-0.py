class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ctr = [0]*3

        for i in nums:
            ctr[i] +=1

        ind = 0 
        for j in range(3) :
            for m in range(ctr[j]) :
                nums[ind] = j
                ind += 1