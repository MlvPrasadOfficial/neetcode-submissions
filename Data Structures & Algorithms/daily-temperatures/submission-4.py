class Solution:

  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # Initialize result array with zeros (days with no warmer future temp will stay 0)
    res = [0] * len(temperatures)
    stack = []  # pair: [temp, index]

    # Enumerate gives us both the index (i) and the temperature value (t)
    for i, t in enumerate(temperatures):

      # While stack is not empty AND the current temperature (t) 
      # is strictly greater than the temperature at the top of the stack
      while stack and t > stack[-1][0]:
        stackT, stackInd = stack.pop()  # Pop the colder day

        # The wait time is the difference between current index (i) and that past index
        res[stackInd] = i - stackInd

      # Push the current temperature and its index onto the stack
      stack.append((t, i))

    return res