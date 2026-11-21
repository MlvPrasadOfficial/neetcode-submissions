class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if either string is empty or t is longer than s, no valid window exists
        if not s or not t or len(t) > len(s):
            return ""

        # Frequency map of characters required from string t
        need = {}
        for ch in t:
            need[ch] = 1 + need.get(ch, 0)

        # Frequency map of characters in the current sliding window [l..r]
        window = {}
        have = 0              # Number of distinct characters meeting their required count
        required = len(need)  # Total distinct characters in t we need to satisfy

        res = [-1, -1]        # Stores [left_index, right_index] of the best window found
        res_len = float("inf")
        l = 0                 # Left pointer of the sliding window

        # Expand the window by moving the right pointer r across s
        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)

            # Increment 'have' only when ch reaches its exact required frequency in t
            if ch in need and window[ch] == need[ch]:
                have += 1

            # Once all required characters are satisfied, try shrinking from the left
            # to find the shortest valid substring
            while have == required:
                # Update best window if current window is shorter
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # Remove the leftmost character and advance l
                left_ch = s[l]
                window[left_ch] -= 1

                # If removing left_ch drops its count below what's needed, window is no longer valid
                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                l += 1

        left_idx, right_idx = res
        return s[left_idx : right_idx + 1] if res_len != float("inf") else ""