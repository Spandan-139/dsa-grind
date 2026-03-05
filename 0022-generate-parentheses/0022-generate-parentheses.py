class Solution:
    def generateParenthesis(self, n: int):
        res = []
        path = []

        def backtrack(open_used: int, close_used: int):
            if open_used == n and close_used == n:
                res.append("".join(path))
                return

            if open_used < n:
                path.append("(")
                backtrack(open_used + 1, close_used)
                path.pop()

            if close_used < open_used:
                path.append(")")
                backtrack(open_used, close_used + 1)
                path.pop()

        backtrack(0, 0)
        return res