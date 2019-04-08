class Solution:
    """
    Leetcode # 529
    BFS solution using queue
    """
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n = len(board)
        m = len(board[0])
        row, col = click
        queue = collections.deque()
        queue.append(click)
        
        while queue:
            row, col = queue.pop()
            if board[row][col] == 'M':
                board[row][col] = 'X'
                
            else:
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        r, c = row+i, col+j

                        if i == 0 and j == 0:
                            continue
                        elif (r<0 or c<0 or r>=n or c>=m):
                            continue
                        elif board[r][c] == 'M' or  board[r][c] == 'X':
                            count += 1
                
                if count > 0:
                    board[row][col] = str(count)
                else:
                    board[row][col] = 'B'
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            r, c = row+i, col+j

                            if i == 0 and j == 0:
                                continue
                            elif (r<0 or c<0 or r>=n or c>=m):
                                continue
                            elif board[r][c] == 'E':
                                board[r][c] = 'B'
                                queue.append([r,c])
                                
        return board
