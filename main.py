import chess
import chess.engine
import random
from datetime import datetime
def userMoves(): 
    return
def botMoves():
    return
def main(): 
    board = chess.Board()
    print(board)
    print("=====================================================\n              CS 290 Chess Bot Version 0.1\n=====================================================")
    print("Time: " , datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    starting_color = input("Computer Player? (w=white/b=black): ")
    starting_FEN = input("Starting FEN position? (hit ENTER for standard starting position): ")

def print_board(board):
    print("Current Board:")
    print(board)
    print("FEN position:", board.fen())

def user_input(board, player_color):
     while True:
        move_input = input(f"{player_color.capitalize()}: ").strip()
         try:
                if move in board.legal_moves:
                return move
            else:
                print("Invalid move. Please enter a legal move in UCI format.")
        except ValueError:
            print("Invalid input format. Please enter move in UCI format (e.g., e2e4).")

    

main()
