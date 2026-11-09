class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        # max 
        m = 0 
        he = heights

        stack = []

        for i,h in enumerate(he) :
            # print(i,h,"----------i","h")
            index = i


            while stack and stack[-1][1] > h :
                li, lh = stack.pop()

                m = max(m, (i-li)*lh)
                index = li


            stack.append([index, h])
            # print(stack, m)

        for a,b in stack :
            m = max(m,(b*(len(he)-a)))

        return m

            



            