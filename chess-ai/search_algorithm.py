from evaluation2 import evaluate_board

# Minimax with alpha-beta pruning
def alphabeta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)

    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval = alphabeta(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = alphabeta(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

def find_best_move(board, depth):
    best_move = None
    maximizing_player = board.turn  # True if White, False if Black

    if maximizing_player:
        best_value = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            board_value = alphabeta(board, depth - 1, float('-inf'), float('inf'), False)
            board.pop()
            if board_value > best_value:
                best_value = board_value
                best_move = move
    else:
        best_value = float('inf')
        for move in board.legal_moves:
            board.push(move)
            board_value = alphabeta(board, depth - 1, float('-inf'), float('inf'), True)
            board.pop()
            if board_value < best_value:
                best_value = board_value
                best_move = move
    if best_move == None:
        return list(board.legal_moves)[0].uci() #validdddd maybe?
    else:
        return best_move
