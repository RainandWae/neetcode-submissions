class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 too long to fit in s2, impossible
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26  # char frequency counters, index = letter (a=0, b=1...)

        # build initial window, first len(s1) chars of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # matches = how many letters (0-25) have equal count in both windows
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        # slide window across rest of s2
        for r in range(len(s1), len(s2)):
            # all 26 letters match, found a permutation
            if matches == 26:
                return True

            # add new right char into window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1  # this letter now matches
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1  # this letter just went from matching to not matching

            # remove old left char from window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1  # this letter now matches
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1  # this letter just went from matching to not matching

            l += 1  # move window forward

        # check one last time after loop ends (window never checked on final iteration)
        return matches == 26