class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]

            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in words:
                    for rest in dfs(end):
                        res.append(word if rest == "" else word + " " + rest)

            memo[start] = res
            return res

        return dfs(0)