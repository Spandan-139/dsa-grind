class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        path = []

        def backtrack(start: int, remain: int) -> None:
            if remain == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    break

                path.append(candidates[i])
                backtrack(i + 1, remain - candidates[i])  # move forward, no reuse
                path.pop()

        backtrack(0, target)
        return res