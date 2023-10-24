# Tic-Tac-Toe AI with Minimax and Alpha-Beta Pruning

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def minimax(board, depth, is_maximizing):
    scores = {
        "X": 1,
        "O": -1,
        "tie": 0
    }

    winner = None

    if check_win(board, "X"):
        winner = "X"
    elif check_win(board, "O"):
        winner = "O"

    if winner:
        return scores[winner]

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ""
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -float("inf")
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def main():
    board = [["" for _ in range(3)] for _ in range(3)
    ]
    player = "X"
    turn = 0

    while True:
        print_board(board)

        if player == "X":
            row, col = find_best_move(board)
        else:
            while True:
                try:
                    row, col = map(int, input(f"Enter row and column (0-2) for '{player}': ").split())
                    if board[row][col] == "":
                        break
                    else:
                        print("Cell already occupied. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Try again.")

        board[row][col] = player

        if check_win(board, player):
            print_board(board)
            print(f"'{player}' wins!")
            break

        turn += 1
        if turn == 9:
            print_board(board)
            print("It's a tie!")
            break

        player = "X" if player == "O" else "O"

if __name__ == "__main__":
    main()
