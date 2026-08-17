class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            # built a string as long as digits, valid combo complete
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            # try every letter mapped to current digit
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)  # move to next digit, append this letter

        # guard against empty input, avoid returning [""]
        if digits:
            backtrack(0, "")
        return res