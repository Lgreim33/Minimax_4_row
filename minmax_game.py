import numpy as np
from board import Board
import time
        
        
WIN = 1000
TIE = 0
LOSS = -1000

PLAYER_1 = 1
PLAYER_2 = 0

# Globally track nodes that are recursively generated
node_count = 0

# generates the successors of the passed game_state
def generate_successors(state, player):
    successors = []
    valid_moves = state.get_valid_moves()
    global node_count
    
    if not valid_moves:
        print(f"No valid moves for player {player}")

    for move in valid_moves:
        next_state = Board()
        next_state.board = np.copy(state.board)  # Create a copy of the current board
        next_state.move(move, player)  # Apply the move
        successors.append((next_state, move))  # Add the new board state and the move to the list
        node_count += 1
    return successors

# recursive minimax, returns the best move to make for the player
def minimax(state, me, is_maxing, depth, alpha, beta):

    global node_count

    if me == PLAYER_1:
        them = PLAYER_2
    elif me == PLAYER_2:
        them = PLAYER_1
    else: raise ValueError("Parameter 'me' must be 0 or 1. Actual:", me)

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
    s, move = minimax(board,PLAYER_1,True,2,alpha=np.float64("-inf"),beta=np.float64("inf"))
    end_time = time.time() - start_time
    
    board.move(move,1)
    print(f"Minimax took: {end_time} seconds")
    print(f"Player 1 Places X at {move} for Score {s}")

    print(f"Nodes generated for Player 1: {node_count}")
    
    return


#handles the monimax call for player 2, takes the board state as an argument, wont return anything
def player_2_move(board):
    global node_count
    node_count = 0
    
    start_time = time.time()
    
    #four ply call for minimax
    s, move = minimax(board,PLAYER_2,True,4,alpha=np.float64("-inf"),beta=np.float64("inf"))
    
    end_time = time.time() - start_time
    
    if move is not None:
        board.move(move, 0)
        print(f"Minimax took: {end_time} seconds")
        print(f"Player 2 Places O at {move} for Score {s}")
    else:
        print("")# print("No valid moves for Player 2")
    
    print(f"Nodes generated for Player 2: {node_count}")

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
    print("Player 1 Moves: ", player_1_init)
    board_world.move(player_1_init,1)
    print(board_world.board)
    
    print("Turn 2")
    print("Player 2 Moves: ", player_2_init)
    board_world.move(player_2_init,0)
    print(board_world.board)
    
    #while the board isnt full and nobody has won, play the game
    while not board_world.is_full(): 
        print(f"Turn {turn}")
        
        #if player one takes odd turns, player 2 takes even turns
        if turn % 2 != 0:
            player_1_move(board_world)
        else:
            player_2_move(board_world)
        
        #print the board after the move
        print(board_world.board)
        
        #check the current board state for both players and check to see if they won
        if board_world.heuristic(True) == WIN:
            print("Player 1 Wins!")
            return 

        if board_world.heuristic(False) == WIN:
            print("Player 2 Wins!")
            return 
        
        turn +=1
    #if we've left the loop, that means teh board is full and nobody won
    print("It's a tie :/")
    return        
    
def test_heuristic():
    aboard = Board()
    aboard.move((1, 2), 0)  # O
    aboard.move((2, 2), 0)  # O
    aboard.move((2, 3), 0)  # O
    aboard.move((3, 4), 0)  # O
    aboard.move((3, 1), 0)  # O

    aboard.move((1, 3), 1)  # X
    aboard.move((3, 3), 1)  # X
    aboard.move((3, 2), 1)  # X
    aboard.move((4, 2), 1)  # X
    aboard.move((2, 4), 1)  # X
 
    print(aboard.board)

    heuristic_value = aboard.heuristic(True)

    print(f"Heuristic value for player X: {heuristic_value}")

    expected_value = 84
    assert heuristic_value == expected_value, f"Expected {expected_value}, but got {heuristic_value}"
    return

# Run the test
# test_heuristic()
start()