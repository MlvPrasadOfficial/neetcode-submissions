class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        h = {}
        for i in s1 :
            if i not in h :
                h[i] = 1
            else :
                h[i] += 1



        for a in range(len(s2)-len(s1)+1) :
            temp = s2[a:a+len(s1)]
            temph = {}
            for b in temp :
                if b not in temph :
                    temph[b] = 1
                else :
                    temph[b] += 1
            if h == temph :
                return True

        return False

        