class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        mi = 10000

        for i in strs :
            mi = min(mi,len(i))

        ans = ""
        for k in range(mi):
            res  = ""
            for j in strs :
                res += j[k]

            if res.count(j[k]) == len(strs) :
                ans += j[k]
            else :
                return ans
        return ans


        