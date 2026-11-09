class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                
                valbit = 1 << int(val)
                boxbit = (r//3)*3 + (c//3)

                if (rows[r] & valbit) or (cols[c] & valbit) or (boxes[boxbit] & valbit):
                    return False
                rows[r]|= valbit
                cols[c]|= valbit
                boxes[boxbit]|= valbit

        return True