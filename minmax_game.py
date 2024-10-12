import numpy as np
from board import Board
import time
        
        
WIN = 1000
TIE = 0
LOSS = -1000

#generates the sucessor of the passed game_state
def generate_sucsessors(board):
    succsessor_list = board.get_valid_moves()
    
    

    


#recursive minimax
def minimax(state,is_maxing,depth,alpha,beta):
    
    
    
    #we are maximizing the heuristic
    if is_maxing:
        return
        
    #minimizing the heuristic
    elif not is_maxing:
        return
    return

#handles the minimax call for player 1, takes the board state as an argument, wont return anything
def player_1_move(board):
    start_time = time.time()
    
    #two ply call for minimax
    
    end_time = time.time() - start_time
    
    return


#handles the monimax call for player 2, takes the board state as an argument, wont return anything
def player_2_move(board):
    
    start_time = time.time()
    
    #four ply call for minimax
    
    end_time = time.time() - start_time
    return 






#driver function for minimax and players
def start():
    #init the board world
    board_world = Board()

    #we will start displaying the actual turn variable after the manual intial moves
    turn = 3
    
    player_1_move = (2,3)
    player_2_move = (2,2)
    
    #initial moves for both players (-1,-1 for indexing)
    print("Turn 1")
    print("Player 1 Moves: ", player_1_move)
    board_world.move(player_1_move,1)
    print(board_world.board)
    
    print("Turn 2")
    print("Player 2 Moves: ", player_2_move)
    board_world.move(player_2_move,0)
    print(board_world.board)
    
    #while the board isnt full and nobody has won, play the game
    while not board_world.is_full(): 
        print(f"Turn {turn}")
        
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
    


start()