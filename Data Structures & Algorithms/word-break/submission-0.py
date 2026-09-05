class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s): True}  # base case, reached end of string = successfully broken it up

        def dfs(i):
            # already computed this, reuse cached result
            if i in memo:
                return memo[i]

            # try every word in dict, see if it fits starting at position i
            for w in wordDict:
                if ((i + len(w)) <= len(s) and
                     s[i : i + len(w)] == w
                ):
                    # word matches here, check if rest of string can also be broken up
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True

            # no word worked from this position, dead end
            memo[i] = False
            return False

        return dfs(0)