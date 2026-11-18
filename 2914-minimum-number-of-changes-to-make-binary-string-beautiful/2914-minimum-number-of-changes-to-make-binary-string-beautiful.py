class Solution(object):
    def minChanges(self, s):
        changes = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                changes += 1
        return changes


# Quick tests
if __name__ == "__main__":
    sol = Solution()
    assert sol.minChanges("1001") == 2
    assert sol.minChanges("10") == 1
    assert sol.minChanges("0000") == 0
    assert sol.minChanges("0110") == 2
    assert sol.minChanges("1111") == 0
    assert sol.minChanges("0101") == 2
    print("All tests passed")