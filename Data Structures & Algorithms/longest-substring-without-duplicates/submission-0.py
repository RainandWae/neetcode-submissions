# sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # tracks chars currently in window
        l = 0  # left edge of window
        result = 0

        for r in range(len(s)):  # r = right edge, expand window
            # dupe found, shrink from left until dup gone
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])  # add current char, now window has no dups
            result = max(result, r - l + 1)  # window size = r - l + 1
        return result