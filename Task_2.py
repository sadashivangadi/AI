# Task 2: Tic Tac Toe AI using Minimax 

import math

# Initialize board
board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def is_winner(brd, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows show
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns show
        [0, 1, 8], [2, 4, 6] ,# diagonals
    ]
    for cond in win_conditions:
        if brd[cond[0]] == brd[cond[1]] == brd[cond[2]] == player:
            return True
    return False

def empty_cells(brd):
    return [i for i, cell in enumerate(brd) if cell == " "]

def minimax(brd, depth, is_maximizing):
    if is_winner(brd, "O"):
        return 1
    if is_winner(brd, "X"):
        return -1
    if len(empty_cells(brd)) == 0:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for pos in empty_cells(brd):
            brd[pos] = "O"
            score = minimax(brd, depth + 1, False)
            brd[pos] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for pos in empty_cells(brd):
            brd[pos] = "X"
            score = minimax(brd, depth + 1, True)
            brd[pos] = " "
            best_score = min(best_score, score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = None

    for pos in empty_cells(board):
        board[pos] = "O"
        score = minimax(board, 0, False)
        board[pos] = " "
        if score > best_score:
            best_score = score
            best_move = pos

    board[best_move] = "O"

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in empty_cells(board):
                board[move] = "X"
                break
            else:
                print("Invalid move! Try again.")
        except:
            print("Please enter a number 1–9.")

# Main Game Loop
print("Welcome to Tic Tac Toe!")
print("You are X. AI is O.")
print_board()

while True:
    # Player Turn
    player_move()
    print_board()

    if is_winner(board, "X"):
        print("🎉 You Win!")
        break

    if len(empty_cells(board)) == 0:
        print("It's a Draw!")
        break

    # AI Turn
    print("AI is thinking...")
    ai_move()
    print_board()

    if is_winner(board, "O"):
        print("🤖 AI Wins!")
        break

    if len(empty_cells(board)) == 0:
        print("It's a Draw!")
        break
