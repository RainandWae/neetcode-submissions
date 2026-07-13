# TWO POINTER
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 # left
        r = len(s) -1 #right

        # loop until middle
        while l < r:
            # check if current letter looking at in
            # range of A to Z unicode value
            # a to z
            # and 0 to 9
            while l < r and not self.alphaNum(s[l]):
                l += 1 # move pointers toward middle
            while r > l and not self.alphaNum(s[r]):
                r -= 1 # move pointers toward middle
            # actual check if current letter/number equal to each other
            if s[l].lower() != s[r].lower(): 
                return False
            l += 1
            r -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))