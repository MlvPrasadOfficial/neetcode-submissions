class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = nums
        n = list(sorted(n))


        for i in range(len(n)) :
            f = n[i] # -4
            l = 0 
            r = len(n)-1 # 5

            while l < r : # 0 < 5
                if l == i : # 1
                    l += 1
                elif r == i : # 5
                    r -= 1

                if l < r :

                    if f + n[l] + n[r] == 0 : # -4 -0 3
                        res.append(tuple(sorted([f,n[l],n[r]])))
                        l += 1
                    elif f + n[l] + n[r] > 0 :
                        r = r - 1
                    elif f + n[l] + n[r] < 0 :# 3
                        l = l + 1
                
        return list(set(res))

        # -4 -1 -1 0 2 3
                
            



        