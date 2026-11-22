class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen = [0] * len(nums) 
        z = 0
        for i in nums :
            z += 1  
            # print(abs(i),"i")       
           
            if nums[abs(i)-1] < 0 :
              return abs(i)

            else :
              nums[abs(i)-1] *= -1


            # print(i,nums)
            # print()
            # if z== 65 :
                # break
        