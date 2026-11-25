class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count = 0
        for p in patterns:
            if p in word:
                count += 1

        return count