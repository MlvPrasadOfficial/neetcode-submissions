class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        from collections import defaultdict

        a = defaultdict(int)
        mx= -1


        for i in nums :
            a[i] +=1

            if a[i] >= mx :
                mx = a[i]
                ans = i

        return ans
                