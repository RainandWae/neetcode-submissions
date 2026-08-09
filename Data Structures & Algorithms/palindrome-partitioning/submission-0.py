class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            # reached end of string, current partition is valid, save it
            if i >= len(s):
                res.append(part.copy())
                return

            # try every possible substring starting at i
            for j in range(i, len(s)):
                # only proceed if s[i:j+1] is a palindrome
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)  # recurse on rest of string after this piece
                    part.pop()  # undo, try next possible length

        dfs(0)
        return res

    def isPali(self, s, l, r):
        # standard two pointer palindrome check
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True