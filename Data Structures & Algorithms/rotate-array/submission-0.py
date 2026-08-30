class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0  # 0
        j = len(nums) - 1 # 7

        while i < j : # 0 < 7 
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            j = j -1
        print(nums)


        # k can be any number 
        k = k % len(nums)

        a = 0
        b = k -1

        # print(b,k)
        while a < b :
            # print(a,b,nums[a])
            nums[a], nums[b] = nums[b], nums[a]
            a = a + 1
            b = b -  1
        a = k
        b = len(nums) - 1
        while a < b :
            # print(a,b,nums[a])
            nums[a], nums[b] = nums[b], nums[a]
            a = a + 1
            b = b -  1
