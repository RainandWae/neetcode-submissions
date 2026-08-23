class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        dp = [[False] * n for _ in range(n)]  # dp[i][j] = True if s[i:j+1] is a palindrome

        # fill bottom-up, i goes backwards so smaller substrings computed before bigger ones
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # s[i:j+1] is palindrome if endpoints match AND inside part is also palindrome
                # (j - i <= 2 handles base cases: single char, or 2-3 chars where middle doesn't matter)
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1  # found another palindromic substring, count it

        return res