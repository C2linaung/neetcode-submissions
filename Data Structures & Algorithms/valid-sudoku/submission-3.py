class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidGrid(c_offset, r_offset) -> bool:
            seen = set()
            for r in range(3):
                r += r_offset
                for c in range(3):
                    c += c_offset
                    if board[r][c] == ".":
                        continue
                    
                    if board[r][c] in seen:
                        return False
                    
                    seen.add(board[r][c])
            return True

        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in seen:
                    return False
                
                seen.add(board[r][c])

        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in seen:
                    return False
                
                seen.add(board[r][c])
        
        for c in range(0, 7, 3):
            for r in range(0, 7, 3):
                if not isValidGrid(c, r):
                    return False

        return True