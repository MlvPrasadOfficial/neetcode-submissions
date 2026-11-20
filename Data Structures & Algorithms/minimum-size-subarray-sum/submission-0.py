class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        l = 0 
        res = float("inf")
        tot = 0 

        for r in range(len(nums)) : # iteratin through all elements
            tot += nums[r]

            while tot >= target :
                res = min(r-l+1,res)

                tot -= nums[l]
                l = l + 1

        if res == float("inf") :
            return 0 
        else :
            return res
    

        