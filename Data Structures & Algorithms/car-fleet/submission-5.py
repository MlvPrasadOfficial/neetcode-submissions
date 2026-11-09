class Solution:

  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    # 1. Pair each car's position with its speed
    pair = [(p, s) for p, s in zip(position, speed)]

    # 2. Sort the cars in reverse order based on their starting positions 
    # (meaning the car closest to the target comes first)
    pair.sort(reverse=True)

    stack = []

    for p, s in pair:  # Reverse Sorted Order
      # 3. Calculate time to reach the target: (target - position) / speed
      stack.append((target - p) / s)

      # 4. Collision / Fleet check:
      # If the car behind (stack[-1]) catches up to or arrives 
      # earlier than the car ahead of it (stack[-2]), they merge into a single fleet!
      if len(stack) >= 2 and stack[-1] <= stack[-2]:
        stack.pop()  # Remove the back car because it merges into the front fleet

    # 5. The total number of fleets left in the stack is our answer
    return len(stack)