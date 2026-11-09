class Solution:

  def shipWithinDays(self, weights: List[int], days: int) -> int:
    # Helper function to check if a given capacity can ship all packages within 'days'
    def can_ship(capacity):
      current_days = 1
      current_load = 0
      for w in weights:
        if current_load + w > capacity:
          current_days += 1
          current_load = w
        else:
          current_load += w
      return current_days <= days

    # Define the binary search range
    low = max(weights)  # Minimum capacity must be at least the heaviest package
    high = sum(
        weights
    )  # Maximum capacity is shipping everything in a single day
    res = high

    while low <= high:
      mid = (low + high) // 2
      if can_ship(mid):
        res = mid  # Valid capacity found, try to find a smaller one
        high = mid - 1
      else:
        low = mid + 1  # Too small, increase capacity

    return res