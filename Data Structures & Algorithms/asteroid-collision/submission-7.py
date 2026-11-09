class Solution:

  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []  # Stores the surviving asteroids

    for a in asteroids:
      # Collision condition:
      # 1. stack is not empty
      # 2. current asteroid 'a' is moving left (a < 0)
      # 3. top of the stack is moving right (stack[-1] > 0)
      while stack and a < 0 and stack[-1] > 0:
        diff = a + stack[-1]  # Compare sizes (absolute values)

        if diff < 0:
          # Current asteroid 'a' is bigger (more negative).
          # The stack asteroid explodes, so we pop it and keep checking 'a' against the next stack element.
          stack.pop()
        elif diff > 0:
          # The stack asteroid is bigger (more positive).
          # Current asteroid 'a' explodes, so we set a = 0 to mark it as destroyed.
          a = 0
        else:
          # Both are equal in size! They both explode.
          # We pop the stack asteroid and destroy 'a' by setting it to 0.
          a = 0
          stack.pop()

      # If 'a' survived all collisions, add it to the stack
      if a:
        stack.append(a)

    return stack