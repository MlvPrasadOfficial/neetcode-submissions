class Solution:
    def trap(self, height: List[int]) -> int:
        h = height

        maxl = [0]*len(h)
        maxr = [0]*len(h)

        mn = height[0]
        mx = height[-1]

        for i in range(len(h)) :
            mn = max(h[i],mn)
            maxl[i] = mn
        for j in range(len(h)-1,-1,-1) :
            mx = max(h[j],mx)
            maxr[j] = mx
        
        minlr = [0]*len(h)

        for p in range(len(h)) :
            temp = min(maxl[p],maxr[p])
            minlr[p] = temp


        area = 0 
        for q in range(len(h)) :
            if minlr[q] - h[q] > 0 :
                area += minlr[q] - h[q]
        return area
