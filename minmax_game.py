import numpy as np
from board import Board
import time
        
        
WIN = 1000
TIE = 0
LOSS = -1000

PLAYER_1 = 1
PLAYER_2 = 0

# globally track recursively-generated nodes
node_count = 0

# generates possible moves after state
def generate_successors(state, player):
    successors = []
    valid_moves = state.get_valid_moves()
    global node_count
    
    if not valid_moves:
        print(f"No valid moves for player {player}")

    for move in valid_moves:
        next_state = Board()
        next_state.board = np.copy(state.board)  # Copy of current board
        next_state.move(move, player)  # Apply the move
        successors.append((next_state, move))  # List contains next_state its corresponding move 
        node_count += 1
    return successors

# recursive minimax, returns the best move to make for the player
def minimax(state, me, is_maxing, depth, alpha, beta):

    global node_count

    if me == PLAYER_1: # Me: Whose Turn it is, Them: Opponent
        them = PLAYER_2
    elif me == PLAYER_2:
        them = PLAYER_1
    else: raise ValueError("Parameter 'me' must be 0 or 1. Actual: ", me)

    # base case
    if depth == 0 or state.is_full():
        return state.heuristic(is_maxing), None
    
    best_move = None

    # maximizing the heuristic
    if is_maxing:
        best_score = np.float64("-inf")
        for successor, move in generate_successors(state, me):  # My lookahead
            score, m = minimax(successor, them, False, depth - 1, alpha, beta)

            if score > best_score:  # max(score, best_score)
                best_score = score
                best_move = move

            alpha = max(alpha, best_score)

            if beta <= alpha:  # Alpha Beta Pruning 
                break

        return best_score, best_move

    # minimizing the heuristic
    else:
        best_score = np.float64("inf")
        for successor, move in generate_successors(state, them):  # Their lookahead
            score, m = minimax(successor, me, True, depth - 1, alpha, beta)

            if score < best_score:  
                best_score = score
                best_move = move

            beta = min(beta, best_score)

            if beta <= alpha:  # Alpha Beta Pruning 
                break

        return best_score, best_move

#handles the minimax call for player 1, takes the board state as an argument, wont return anything
def player_1_move(board):
    global node_count
    node_count = 0

    start_time = time.time()
    
    #two ply call for minimax
    s, move = minimax(board, PLAYER_1, True, 2, alpha=np.float64("-inf"), beta=np.float64("inf"))
    end_time = time.time() - start_time

    if move is not None:
        board.move(move, 1)
        print("Player 1 Places X at", format_move(move))
        print(format_board(board.board))
    else:
        print("No valid moves for Player 1")
    
    print(f"Minimax took: {end_time} seconds")
    print(f"Nodes generated for Player 1: {node_count}")
    print("-----") 
    return

# Some extra format functions for print that aren't part of Board.py
def format_board(board): # Let { nan -> . , 1 -> x , 0 -> o }
    formatted_rows = []
    for row in board:
        formatted_row = ["." if np.isnan(cell) else "x" if cell == 1 else "o" for cell in row]
        formatted_rows.append(" ".join(formatted_row))
    string = "\n".join(formatted_rows)
    return string

def format_move(move): return f"{[move[0] + 1, move[1] + 1]}"

#handles the minimax call for player 2, takes the board state as an argument, wont return anything
def player_2_move(board):
    global node_count
    node_count = 0
    
    start_time = time.time()
    
    #four ply call for minimax
    s, move = minimax(board, PLAYER_2, True, 4, alpha=np.float64("-inf"), beta=np.float64("inf"))
    
    end_time = time.time() - start_time
    
    if move is not None:
        board.move(move, 0)
        print("Player 2 Places O at", format_move(move))
        print(format_board(board.board))
    else:
        print("No valid moves for Player 2")
    
    print(f"Minimax took: {end_time} seconds")
    print(f"Nodes generated for Player 2: {node_count}")
    print("-----")
    return 

#driver function for minimax and players
def start():
    #init the board world
    board_world = Board()

    #we will start displaying the actual turn variable after the manual intial moves
    turn = 3
    
    player_1_init = (2,3)
    player_2_init = (2,2)
    
    #initial moves for both players (-1,-1 for indexing)
    print("Turn 1")
    print("Player 1 Places X at", format_move(player_1_init))
    board_world.move(player_1_init,1)
    print(format_board(board_world.board))
    print("-----")
    
    print("Turn 2")
    print("Player 2 Places O at", format_move(player_2_init))
    board_world.move(player_2_init,0)
    print(format_board(board_world.board))
    print("-----")
    
    #while the board isnt full and nobody has won, play the game
    while not board_world.is_full(): 
        print(f"Turn {turn}")
        
        #if player one takes odd turns, player 2 takes even turns
        if turn % 2 != 0:
            player_1_move(board_world)
        else:
            player_2_move(board_world)
        
        #check the current board state for both players and check to see if they won
        if board_world.heuristic(True) == WIN:
            print("Player 1 Wins!")
            return 

        if board_world.heuristic(False) == WIN:
            print("Player 2 Wins!")
            return 
        
        turn +=1
    #if we've left the loop, that means the board is full and nobody won
    print("It's a tie :/")
    return        

# Run the test
start()