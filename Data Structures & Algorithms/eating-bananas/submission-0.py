class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        a = 1
        b = max(piles)

        res = b # def ans

        while a <= b :

            mid = (a + b)//2
            time = 0 


            for p in piles :
                time += math.ceil(float(p)/mid)
            if time <= h :
                res = mid 
                b = mid -1
            else :
                a = mid + 1
        return res


        