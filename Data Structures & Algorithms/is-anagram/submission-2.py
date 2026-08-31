class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        ref1 = {}
        ref2 = {}


        for i in s :
            if i in ref1 :
                ref1[i] += 1
            else :
                ref1[i] = 1
        for j in t :
            if j in ref2 :
                ref2[j] += 1
            else :
                ref2[j] = 1

        if ref1 == ref2 :
            return True
        return False