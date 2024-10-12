import numpy as np
from board import Board
import time
        
        
WIN = 1000
TIE = 0
LOSS = -1000

#generates the sucessor of the passed game_state
def generate_sucsessors(board):
    succsessor_list = board.get_valid_moves()
    
    

    


#recursive minimax, returns the best move to make for the player
def minimax(state,is_maxing,depth,alpha,beta):
    
    #base case
    if(depth == 0):
        return 
    
    #we are maximizing the heuristic
    if is_maxing:
        print("Player 1 is Maxing")
        return
        
    #minimizing the heuristic
    elif not is_maxing:
        print("Player 2 is Mining")
        return
    return

#handles the minimax call for player 1, takes the board state as an argument, wont return anything
def player_1_move(board):
    start_time = time.time()
    
    #two ply call for minimax
    move = minimax(board,True,2,alpha=np.float("-inf"),beta=("inf"))
    
    end_time = time.time() - start_time
    
    board.move(move,1)
    print(f"Minimax took: {end_time} seconds")
    print(f"Player 1 Places X at {move}")
    
    return


#handles the monimax call for player 2, takes the board state as an argument, wont return anything
def player_2_move(board):
    
    start_time = time.time()
    
    #four ply call for minimax
    move = minimax(board,False,4,alpha=np.float("-inf"),beta=("inf"))
    
    end_time = time.time() - start_time
    
    board.move(move,0)
    print(f"Minimax took: {end_time} seconds")
    print(f"Player 2 Places O at {move}")
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
    


start()