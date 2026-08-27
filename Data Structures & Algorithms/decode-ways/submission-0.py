class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}  # base case, empty string left = 1 way (successfully decoded everything)

        def dfs(i):
            # already computed this, reuse cached result
            if i in dp:
                return dp[i]

            # leading zero can't be decoded on its own, dead end
            if s[i] == "0":
                return 0

            # take 1 digit as a letter, recurse on rest
            res = dfs(i + 1)

            # check if 2 digits together form valid letter (10-26)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)  # take 2 digits together, recurse on rest

            dp[i] = res  # cache result
            return res

        return dfs(0)