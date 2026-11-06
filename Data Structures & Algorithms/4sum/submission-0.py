class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        t = target 
        n = nums
        n = list(sorted(n))

        res = []  
        if len(n) < 4 :
            return [] 

        for  i in range(len(n)-3) : # len(n) = 6 -- o to 5(n-1)
            f1 = n[i]
            for j in range(i+1,len(n)-2) :
                f2 = n[j] 

                l = j+ 1
                r = len(n)-1

                while l < r :
                    if f1 + f2 + n[l] + n[r] == t:
                        res.append(tuple([f1,f2,n[l],n[r]]))
                        l +=1
                    elif f1 + f2 + n[l] + n[r] < t:
                        l += 1
                    elif f1 + f2 + n[l] + n[r] > t:
                        r -= 1
        return list(set(res))

