class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] in seen:
                    return False

                seen.add(board[r][c])
        
        # check cols
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] in seen:
                    return False

                seen.add(board[r][c])
        
        # check grids
        for x in range(0,9,3):
            for y in range(0,9,3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        if board[x + r][y + c] == '.':
                            continue
                        
                        if board[x + r][y + c] in seen:
                            return False

                        seen.add(board[x + r][y + c])
        return True
