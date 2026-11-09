class Solution:

  def largestRectangleArea(self, heights: List[int]) -> int:
    max_area = 0
    stack = []  # stores pairs of (index, height)

    for i, h in enumerate(heights):
      start = i
      # While stack is not empty and current height is less than the stack's top height
      while stack and stack[-1][1] > h:
        index, height = stack.pop()
        # Calculate area with the popped height
        # Width is current index 'i' minus the index where that bar could stretch back to
        max_area = max(max_area, height * (i - index))
        start = index  # Expand the current shorter bar's start position backward

      stack.append((start, h))

    # Clean up any remaining bars left in the stack
    for index, height in stack:
      max_area = max(max_area, height * (len(heights) - index))

    return max_area