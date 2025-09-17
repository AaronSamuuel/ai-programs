# Tic Tac Toe with Minimax AI

board = [' ' for _ in range(9)]


def print_board():
    row1 = '|'.join(board[0:3])
    row2 = '|'.join(board[3:6])
    row3 = '|'.join(board[6:9])
    print(row1)
    print('-' * 5)
    print(row2)
    print('-' * 5)
    print(row3)


def is_victory(icon):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    return any(board[a] == board[b] == board[c] == icon for a, b, c in win_combinations)


def is_draw():
    return ' ' not in board


def game_over(state):
    return is_victory("X") or is_victory("O") or is_draw()


def evaluate(state):
    if is_victory("X"):
        return 1
    elif is_victory("O"):
        return -1
    else:
        return 0


def get_possible_moves(state):
    return [i for i in range(9) if state[i] == ' ']


def make_move(state, move, player):
    new_state = state[:]
    new_state[move] = player
    return new_state


def minimax(state, depth, player):
    if depth == 0 or game_over(state):
        return evaluate(state)

    if player == "X":  # Maximizing player
        best_score = float('-inf')
        for move in get_possible_moves(state):
            new_state = make_move(state, move, "X")
            score = minimax(new_state, depth - 1, "O")
            best_score = max(best_score, score)
        return best_score
    else:  # Minimizing player
        best_score = float('inf')
        for move in get_possible_moves(state):
            new_state = make_move(state, move, "O")
            score = minimax(new_state, depth - 1, "X")
            best_score = min(best_score, score)
        return best_score


def best_move():
    best_score = float('-inf')
    move = None
    for i in get_possible_moves(board):
        new_state = make_move(board, i, "X")
        score = minimax(new_state, 5, "O")  # depth=5 is enough for Tic Tac Toe
        if score > best_score:
            best_score = score
            move = i
    return move


# --- Game Loop: Human (O) vs AI (X) ---
while True:
    print_board()

    # AI Move
    ai_move = best_move()
    if ai_move is not None:
        board[ai_move] = "X"
        if is_victory("X"):
            print_board()
            print("AI (X) Wins! 🎉")
            break
        elif is_draw():
            print_board()
            print("It's a Draw! 🤝")
            break

    print_board()

    # Human Move
    human_move = int(input("Enter your move (1-9): ")) - 1
    if board[human_move] == " ":
        board[human_move] = "O"
    else:
        print("Invalid move! Try again.")
        continue

    if is_victory("O"):
        print_board()
        print("You (O) Win! 🎉")
        break
    elif is_draw():
        print_board()
        print("It's a Draw! 🤝")
        break
