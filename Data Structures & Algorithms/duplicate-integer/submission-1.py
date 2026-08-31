class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        temp = {}


        for i in nums :
            if i in temp :
                if temp[i] ==1 :
                    return True

            else :
                temp[i] = 1

        return False

            