class Solution:

  def decodeString(self, s: str) -> str:
    stack = []
    current_string = ""
    current_num = 0

    for char in s:
      if char.isdigit():
        # Build the number (handles multi-digit numbers like "12")
        current_num = current_num * 10 + int(char)
      elif char == "[":
        # Push the current state onto the stack and reset for the new nested level
        stack.append((current_string, current_num))
        current_string = ""
        current_num = 0
      elif char == "]":
        # Pop the previous string and the multiplier from the stack
        prev_string, num = stack.pop()
        # Decode the current string and append it to the previous string
        current_string = prev_string + current_string * num
      else:
        # It's a lowercase letter, just add it to our current string
        current_string += char

    return current_string