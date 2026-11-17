class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        need = Counter(t)
        missing = len(t)          # characters still needed (with duplicates)
        best_start, best_len = 0, float("inf")

        left = 0
        for right, ch in enumerate(s):
            # Expand: take s[right] into the window
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            # Window is valid: shrink from the left as far as possible
            if missing == 0:
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if right - left + 1 < best_len:
                    best_start, best_len = left, right - left + 1

                # Drop s[left] to look for the next valid window
                need[s[left]] += 1
                missing += 1
                left += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]


# Quick checks
if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))  # BANC
    print(sol.minWindow("a", "a"))                # a
    print(sol.minWindow("a", "aa"))  