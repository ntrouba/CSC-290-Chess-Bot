import chess
import chess.engine
import random
from datetime import datetime
    
def botMoves(board):
    capture_moves = [move for move in board.legal_moves if board.is_capture(move)]
    if capture_moves:
        return random.choice(capture_moves)
    else:
        return random.choice(list(board.legal_moves))
    
def main(): 
    board = chess.Board()
    #print(board)
    print(board.legal_moves)
    
    print("=====================================================\n              CS 290 Chess Bot Version 0.1\n=====================================================")
    print("Time: " , datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    player_color = input("Computer Player? (w=white/b=black): ")
    starting_FEN = input("Starting FEN position? (hit ENTER for standard starting position): ")
    while True:
        user_input(board, player_color)
        print(board.turn)
        if board.turn != player_color: 
            print(board.turn)


def print_board(board):
    print("Current Board:")
    print(board)
    print("FEN position:", board.fen())
def update_board(board, move): 
    print(board)
    board.push_san(move.uci())
    print(board)
    return 
def user_input(board, player_color):
        move_input = input(f"{player_color.capitalize()}: ").strip()
        move = chess.Move.from_uci(move_input) 
        try:
            if move in board.legal_moves:
                update_board(board, move)
                return move
            else:
                print("Invalid move. Please enter a legal move in UCI format.")
        except ValueError:
            print("Invalid input format. Please enter move in UCI format (e.g., e2e4).")

    

main()

