class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:


        r = []


        for a in asteroids :
            while r and r[-1] > 0 and a < 0 :
                diff = a + r[-1]
                if diff < 0 :
                    r.pop()
                    # add it to r
                elif diff > 0 :
                    a = 0
                    # ignore new one
                elif diff == 0 :
                    a = 0 
                    r.pop()


            if a != 0 :
                r.append(a)
        return r

