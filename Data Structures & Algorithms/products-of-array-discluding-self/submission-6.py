class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        pr = 1
        zpr = 0
        czr = 0

        for i in nums :
            if i == 0 :
                czr += 1
            if i != 0:
                pr = pr * i
            else :
                zpr = 1
        if czr >=2 :
            return [0]*len(nums)

        for j in range(len(nums)) :
            if zpr == 1 :
                if nums[j] != 0 :
                    nums[j] = 0
                else :
                    nums[j] = pr
            else :
                nums[j] =int(pr/nums[j])
            

        return nums
        