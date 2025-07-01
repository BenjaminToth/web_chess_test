import chess

# Material values
piece_values = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 0  #???????
}

pawn_mg = [
    [0,   0,   0,   0,   0,   0,   0,   0],
    [98, 134,  61,  95,  68, 126, 139,  38],
    [7,  -6,  13,  31,  34,  -2,   0,  -8],
    [-17, 11,   2,  -4,  -4,   1,  -5,  -7],
    [-26,  3,  10,   9,   6,   1,   0,  -5],
    [-22,  9,   5, -11, -10,  -2,   3,  -1],
    [-12,  5,  -3,   1,   0,  -4,   2,   7],
    [0,   0,   0,   0,   0,   0,   0,   0]
]

pawn_eg = [
    [0,   0,   0,   0,   0,   0,   0,   0],
    [178, 173, 158, 134, 147, 132, 165, 187],
    [94, 100,  85,  67,  56,  53,  82,  84],
    [32,  24,  13,   5,  -2,   4,  17,  17],
    [13,   9,  -3,  -5,  -5,  -2,   7,   0],
    [6,   3,   1,  -2,  -3,  -1,  -1,   2],
    [4,   7,   7, -10,  -7,   1,   2,   6],
    [0,   0,   0,   0,   0,   0,   0,   0]
]

knight_mg = [
    [-167, -89, -34, -49, 61, -97, -15, -107],
    [-73, -41, 72, 36, 23, 62, 7, -17],
    [-47, 60, 37, 65, 84, 129, 73, 44],
    [-9, 17, 19, 53, 37, 69, 18, 22],
    [-13, 4, 16, 13, 28, 19, 21, -8],
    [-23, -9, 12, 10, 19, 17, 25, -16],
    [-29, -53, -12, -3, -1, 18, -14, -19],
    [-105, -21, -58, -33, -17, -28, -19, -23]
]

knight_eg = [
    [-58, -38, -13, -28, -31, -27, -63, -99],
    [-25, -8, -25, -2, -9, -25, -24, -52],
    [-24, -20, 10, 9, -1, -9, -19, -41],
    [-17, 3, 22, 22, 22, 11, 8, -18],
    [-18, -6, 16, 25, 16, 17, 4, -18],
    [-23, -3, -1, 15, 10, -3, -20, -22],
    [-42, -20, -10, -5, -2, -20, -23, -44],
    [-29, -51, -23, -15, -22, -18, -50, -64]
]

bishop_mg = [
    [-29, 4, -82, -37, -25, -42, 7, -8],
    [-26, 16, -18, -13, 30, 59, 18, -47],
    [-16, 37, 43, 40, 35, 50, 37, -2],
    [-4, 5, 19, 50, 37, 37, 7, -2],
    [-6, 4, 26, 34, 20, 20, 0, -5],
    [3, -1, 20, 18, 25, 24, 15, -2],
    [-6, -7, -9, 6, -10, -5, -5, -6],
    [-88, -53, -34, -21, -11, -14, -24, -44]
]

bishop_eg = [
    [-14, -21, -11, -8, -7, -9, -17, -24],
    [-8, -4, 7, -12, -3, 4, 3, -22],
    [2, -8, -4, -2, -1, 3, -4, -16],
    [-2, -6, 1, 9, 5, -4, -1, -13],
    [-1, -4, -2, -2, -2, -2, -4, -1],
    [-3, -7, -4, -2, -2, -4, -6, -3],
    [-8, -4, -5, -3, -3, -5, -4, -8],
    [-8, -4, -5, -3, -3, -5, -4, -8]
]

rook_mg = [
    [32, 42, 32, 51, 63, 9, 31, 43],
    [27, 32, 58, 62, 80, 67, 26, 44],
    [-5, 19, 26, 36, 17, 45, 61, 16],
    [-24, -11, 7, 26, 24, 35, -8, -20],
    [-36, -26, -12, -1, 9, -7, 6, -23],
    [-45, -25, -16, -17, 3, 0, -5, -33],
    [-44, -16, -20, -9, -1, 11, -6, -71],
    [-19, -13, 1, 17, 16, 7, -37, -26]
]

rook_eg = [
    [13, 10, 18, 15, 12, 12, 8, 5],
    [11, 13, 13, 11, -3, 3, 8, 3],
    [7, 7, 7, 5, 4, -3, -5, -3],
    [4, 3, 13, 1, 2, 1, -1, 2],
    [3, 5, 8, 4, -5, -6, -8, -11],
    [-4, 0, -5, -1, -7, -12, -8, -16],
    [-6, -6, 0, 2, -9, -9, -11, -3],
    [-9, 2, 3, -1, -5, -13, 4, -20]
]

queen_mg = [
    [-28, 0, 29, 12, 59, 44, 43, 45],
    [-24, -39, -5, 1, -16, 57, 28, 54],
    [-13, -17, 7, 8, 29, 56, 47, 57],
    [-27, -27, -16, -16, -1, 17, -2, 1],
    [-9, -26, -9, -10, -2, -4, 3, -3],
    [-14, 2, -11, -2, -5, 2, 14, 5],
    [-35, -8, 11, 2, 8, 15, -3, 1],
    [-1, -18, -9, 10, -15, -25, -31, -50]
]

queen_eg = [
    [-9, 22, 22, 27, 27, 19, 10, 20],
    [-17, 20, 32, 41, 58, 25, 30, 0],
    [-20, 6, 9, 49, 47, 35, 19, 9],
    [3, 22, 24, 45, 57, 40, 57, 36],
    [-18, 28, 19, 47, 31, 34, 39, 23],
    [-27, -11, 4, 10, 22, 6, -3, -14],
    [-26, -27, -9, -5, -2, -17, -9, -23],
    [-16, -28, -9, -8, -7, -9, -15, -17]
]

king_mg = [
    [-65, 23, 16, -15, -56, -34, 2, 13],
    [29, 45, 61, -24, -35, -22, 10, 19],
    [-15, -16, 0, -15, -12, -14, -15, -11],
    [-17, -27, -13, -27, -30, -25, -14, -36],
    [-49, -1, -27, -39, -46, -44, -33, -51],
    [-14, -14, -22, -46, -44, -30, -15, -27],
    [19, 15, 11, 0, -6, -11, 6, 2],
    [-96, -113, -113, -108, -69, -47, -41, -87]
]

king_eg = [
    [-74, -35, -18, -18, -11, -8, 7, 14],
    [-12, 17, 14, 17, 17, 38, 23, 36],
    [10, 17, 23, 15, 20, 45, 44, 46],
    [40, 41, 52, 37, 46, 52, 36, 26],
    [29, 28, 29, 26, 34, 30, 24, 24],
    [23, 24, 19, 20, 25, 27, 15, 10],
    [4, -17, -4, -31, 1, 4, -5, -22],
    [-27, -39, -46, -53, -50, -43, -39, -46]
]



piece_square_tables_mg = {
    (chess.PAWN): pawn_mg,
    (chess.KNIGHT): knight_mg,
    (chess.BISHOP): bishop_mg,
    (chess.ROOK): rook_mg,
    (chess.QUEEN): queen_mg,
    (chess.KING): king_mg,
}

piece_square_tables_eg = {
    (chess.PAWN): pawn_eg,
    (chess.KNIGHT): knight_eg,
    (chess.BISHOP): bishop_eg,
    (chess.ROOK): rook_eg,
    (chess.QUEEN): queen_eg,
    (chess.KING): king_eg,
}

def calculate_phase(board):
    PHASE_WEIGHTS = {
        chess.KNIGHT: 1,
        chess.BISHOP: 1,
        chess.ROOK: 2,
        chess.QUEEN: 4
    }

    phase = 0
    for piece_type, weight in PHASE_WEIGHTS.items():
        count = len(board.pieces(piece_type, chess.WHITE)) + len(board.pieces(piece_type, chess.BLACK))
        phase += count * weight

    return min(phase, 24)

# Evaluate position
def evaluate_board(board):
    
    # Checking checkmate
    if board.is_checkmate():
        if board.turn:
            return float('-inf')
        else:
            return float('inf') 
    # Checking draw situations
    if board.is_stalemate() or board.is_insufficient_material() or board.can_claim_fifty_moves() or board.can_claim_threefold_repetition():
        return 0

    eval_mg = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_type = piece.piece_type
            color = piece.color
            value = piece_values[piece_type]
            row = chess.square_rank(square)
            col = chess.square_file(square)

            pst = piece_square_tables_mg.get((piece_type))
            pst_value = 0
            if pst:
                if color == chess.WHITE:
                    pst_value = pst[row][col]
                else:
                    pst_value = pst[7 - row][col]  # Flip for black

            if color == chess.WHITE:
                eval_mg += value + pst_value
            else:
                eval_mg -= value + pst_value

    eval_eg = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_type = piece.piece_type
            color = piece.color
            value = piece_values[piece_type]
            row = chess.square_rank(square)
            col = chess.square_file(square)

            pst = piece_square_tables_eg.get((piece_type))
            pst_value = 0
            if pst:
                if color == chess.WHITE:
                    pst_value = pst[row][col]
                else:
                    pst_value = pst[7 - row][col]  # Flip for black

            if color == chess.WHITE:
                eval_eg += value + pst_value
            else:
                eval_eg -= value + pst_value
        phase = calculate_phase(board)
        #print(f"phase: {phase}") TODO testing
    return (eval_mg * phase + eval_eg * (24 - phase)) / 24