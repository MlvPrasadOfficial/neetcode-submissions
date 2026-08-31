class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        temp ={}


        for i,j in enumerate(nums) :
            diff = target - j 
            if diff not in temp :
                temp[j] = i
            elif diff in temp :
                return [temp[diff],i] 
