class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []

        def backtrack(start: int, remain: int) -> None:
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, remain - candidates[i])   # reuse allowed
                path.pop()

        backtrack(0, target)
        return res