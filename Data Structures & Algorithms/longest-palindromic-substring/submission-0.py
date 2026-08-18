class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0  # tracks starting index + length of longest palindrome found
        n = len(s)
        dp = [[False] * n for _ in range(n)]  # dp[i][j] = True if s[i:j+1] is a palindrome

        # fill bottom-up, i goes backwards so smaller substrings computed before bigger ones
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # s[i:j+1] is palindrome if endpoints match AND inside part is also palindrome
                # (j - i <= 2 handles base cases: single char, or 2-3 chars where middle doesn't matter)
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    # found a longer palindrome, update result
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1

        return s[resIdx : resIdx + resLen]