class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures


        res = [0]*len(t)
        s = [] # store (temp,index)

        for i, t in enumerate(t) :
            while s and t > s[-1][0] :
                st,si = s.pop()
                res[si] = i - si
            s.append((t,i))

        return res       