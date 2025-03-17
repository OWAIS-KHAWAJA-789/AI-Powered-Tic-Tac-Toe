import math

def print_board(board):
    """Display the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def is_winner(board, player):
    """Check if the given player has won the game."""
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_draw(board):
    """Check if the game is a draw."""
    return all([cell != ' ' for row in board for cell in row])

def get_available_moves(board):
    """Return a list of available moves."""
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                moves.append((row, col))
    return moves

def minimax(board, depth, is_maximizing):
    """Implement the Minimax algorithm to evaluate the board state."""
    if is_winner(board, 'O'):
        return 10 - depth
    if is_winner(board, 'X'):
        return depth - 10
    if is_draw(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = 'O'
            score = minimax(board, depth + 1, False)
            board[row][col] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = 'X'
            score = minimax(board, depth + 1, True)
            board[row][col] = ' '
            best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    """Find the best move for the AI player using Minimax."""
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        row, col = move
        board[row][col] = 'O'
        score = minimax(board, 0, False)
        board[row][col] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    """Run the game loop allowing a human to play against the AI."""
    # Welcome message
    print("Hey, Welcome to Tic-Tac-Toe by AP2KMO!")
    print("Check out my open source projects on GitHub: github.com/OWAIS-KHAWAJA-789")
    print("You are playing as 'X', and the AI is playing as player 'O'.")
    print("To quit the game, enter 'c'. \n")
    
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        
        if current_player == 'X':
            # Get valid row input
            while True:
                row_input = input("Enter the row (0, 1, or 2) or 'c' to quit: ")
                if row_input.lower() == 'c':
                    print("You have exited the game.")
                    return  # Exit the game
                
                try:
                    row = int(row_input)
                    if row not in [0, 1, 2]:
                        print("Invalid row. Please enter a number between 0 and 2.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    continue
                
                # Get valid column input
                col_input = input("Enter the column (0, 1, or 2) or 'c' to quit: ")
                if col_input.lower() == 'c':
                    print("You have exited the game.")
                    return  # Exit the game
                
                try:
                    col = int(col_input)
                    if col not in [0, 1, 2]:
                        print("Invalid column. Please enter a number between 0 and 2.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    continue
                
                # Check if the selected cell is empty
                if board[row][col] != ' ':
                    print("This cell is already taken. Try again.")
                else:
                    break
            board[row][col] = 'X'
        else:
            best_move = find_best_move(board)
            if best_move:
                row, col = best_move
                board[row][col] = 'O'
        
        if is_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()
