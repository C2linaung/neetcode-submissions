class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check Rows
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        # Check Cols
        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        # Check Grids
        for row_offset in range(3):
            for col_offset in range(3):
                seen = set()
                for r in range(3*row_offset, 3*row_offset + 3, 1):
                    for c in range(3*col_offset, 3*col_offset + 3, 1):
                        val = board[r][c]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)

        return True