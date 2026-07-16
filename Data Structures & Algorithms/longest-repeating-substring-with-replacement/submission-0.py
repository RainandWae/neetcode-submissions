# Sliding window

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        # all unique chars in s
        charSet = set(s)

        # try every char as "the majority char" we keep
        # replace everything else
        for c in charSet:
            # count = how many of char c in current window, l = left edge
            count = l = 0

            for r in range(len(s)):  # r = right edge, expand window
                if s[r] == c:
                    count += 1  # found another c in window

                # window size - count(c) = how many chars need replacing
                # if that's more than k allowed replacements, shrink window
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1  # losing a c as we shrink from left
                    l += 1

                # valid window (replacements needed <= k), track max size
                result = max(result, r - l + 1)
        return result