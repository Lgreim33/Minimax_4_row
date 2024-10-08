import numpy as np
from board import Board

        
        
    

#generates the sucessor of the passed game_state
def generate_sucsessors(board):
    succsessor_list = []
    

    
    
    

'''200*[number of two-side-open-3-in-a-row for me]
– 80*[number of two-side-open-3-in-a-row for opponent]
+ 150*[number of one-side-open-3-in-a-row for me]
– 40*[number of one-side-open-3-in-a-row for opponent]
+ 20*[number of two-side-open-2-in-a-row for me]
– 15*[number of two-side-open-2-in-a-row for opponent]
+ 5*[number of one-side-open-2-in-a-row for me]'''
def calc_heuristic():
    return

#recursive minimax
def minimax(state,is_maxing,depth):
    
    
    
    #we are maximizing the heuristic
    if is_maxing:
        return
        
    #minimizing the heuristic
    elif not is_maxing:
        return
    return


#init the board world
board_world = Board()

#initial moves for both players (-1,-1 for indexing)
board_world.move((2,3),1)
board_world.move((2,2),0)
board_world.move((2,4),1)
board_world.move((1,4),1)
board_world.move((3,5),1)


horizontal,vertical,bl_tr,br_tl = board_world.in_a_row(1)
print("hor ", horizontal,"vert ",vertical, "bl_tr " , bl_tr, "br_tl ",br_tl)


print(board_world.is_valid_move((2,3)))



print(board_world.board)





