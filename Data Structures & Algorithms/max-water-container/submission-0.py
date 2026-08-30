class Solution:
    def maxArea(self, heights: List[int]) -> int:


        m = 0

        i = 0 
        j = len(heights) - 1


        while i < j :
            l = j - i 
            b = min(heights[i],heights[j])

            a = l * b 

            if a > m :
                m = a 

            if heights[i] <= heights[j] :
                i = i + 1
            else :
                j = j - 1
            
        return m 


        