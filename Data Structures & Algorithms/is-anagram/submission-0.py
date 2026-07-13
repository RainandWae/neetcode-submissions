class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check length first, easy sign of nonAnagram
        if len(s) != len(t):
            return False

        #creat count dictionary
        countS, countT = {}, {}

        # go through every letter in [s] and [t]
        # add dictionary count for every unique letter
        # ==> {[r,2] [a, 1], ...}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        # compare and return false true