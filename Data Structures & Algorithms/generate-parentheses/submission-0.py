class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []  # builds current combination of parens
        res = []

        def backtrack(openN, closedN):
            # used exactly n open and n closed, valid combo complete
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # only add open paren if we haven't used all n yet
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            # only add close paren if there are unmatched opens to close
            # (closedN < openN ensures we never close more than we've opened)
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res