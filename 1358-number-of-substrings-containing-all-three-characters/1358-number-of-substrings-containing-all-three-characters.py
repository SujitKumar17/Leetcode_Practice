class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = [-1, -1, -1]
        count = 0
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i
            count += min(last) + 1

        return count