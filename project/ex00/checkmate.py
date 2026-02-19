def is_in_check(board):
    size = len(board)

    # 1) หา King
    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        return False

    ki, kj = king_pos

    directions = {
        'rook': [(-1,0), (1,0), (0,-1), (0,1)],
        'bishop': [(-1,-1), (-1,1), (1,-1), (1,1)],
        'knight': [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    }

    # 2) ตรวจ Pawn
    for dx, dy in [(-1, -1), (-1, 1)]:
        ni, nj = ki + dx, kj + dy
        if 0 <= ni < size and 0 <= nj < size and board[ni][nj] == 'P':
            return True

    # 3) ตรวจ Rook และ Queen
    for dx, dy in directions['rook']:
        x, y = ki + dx, kj + dy
        while 0 <= x < size and 0 <= y < size:
            if board[x][y] != '.':
                if board[x][y] in ('R', 'Q'):
                    return True
                break
            x += dx
            y += dy

    # 4) ตรวจ Bishop และ Queen
    for dx, dy in directions['bishop']:
        x, y = ki + dx, kj + dy
        while 0 <= x < size and 0 <= y < size:
            if board[x][y] != '.':
                if board[x][y] in ('B', 'Q'):
                    return True
                break
            x += dx
            y += dy

    # 5) ตรวจ Knight
    for dx, dy in directions['knight']:
        ni, nj = ki + dx, kj + dy
        if 0 <= ni < size and 0 <= nj < size and board[ni][nj] == 'N':
            return True

    return False
