# REVERSE STRING

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            # isalnum return true if all character are letter/number
            # and must contain letter/number
            if c.isalnum():
                #lower case all string
                newStr += c.lower()
        # compare newStr with a reverse, if it reverse return T/F
        return newStr == newStr[::-1]