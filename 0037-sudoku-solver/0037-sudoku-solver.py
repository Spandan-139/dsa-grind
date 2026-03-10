class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Initialize sets and collect empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(i: int) -> bool:
            if i == len(empties):
                return True

            r, c = empties[i]
            box = (r // 3) * 3 + (c // 3)

            for ch in "123456789":
                if ch in rows[r] or ch in cols[c] or ch in boxes[box]:
                    continue

                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[box].add(ch)

                if backtrack(i + 1):
                    return True

                board[r][c] = "."
                rows[r].remove(ch)
                cols[c].remove(ch)
                boxes[box].remove(ch)

            return False

        backtrack(0)