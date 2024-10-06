import numpy as np
#comment to check git 

class Board:
    LENGTH = 6
    HEIGHT = 5
    #terminal case values
    WIN = 1000
    LOSS = -1000
    TIE = 0
    #refernece to board
    board = None
    book = int()
    
    def __init__(self):
        #if value is not 0 or 1 it is empty, 0 will be Os and 1 will be Xs
        self.board = np.empty((self.HEIGHT,self.LENGTH))
        self.board[:] = np.NaN
        
        
    def move(self,coordinate,player:bool):
        self.board[coordinate[0]][coordinate[1]] = player
        
    #is the move valid
    def is_valid_move(self,coord):
        return (coord[0] < 5 and coord[1] < 6 and np.isnan(self.board[coord[0]][coord[1]]))
            
    #this will be used to generate the sucessors of the current game state        
    def get_valid_moves(self,player:bool):
        return 
            
        
    def is_full(self):
        if True in np.isnan(self.board):
            return False
        else: 
            return True
    
    
    #helper function for heuristic calculation    
    def in_a_row(self,player:bool):
        rows = set()
        list_of_rows = list()
        
        
        
        return 
    
    
    #helper function for heuristic calculation  
    def sides_open(self,in_row_coordinates: list , player:bool):
        return
        
    def heuristic(self,player:bool):
        two_side_three_row_me = 0
        two_side_three_row_opponent = 0
        one_side_three_row_me = 0
        one_side_three_row_opponent = 0
        two_side_two_row_me = 0
        two_side_two_row_opponent = 0
        one_side_two_row_me = 0
        
        
        self.board
        
        
        
        return 
        
        
        
    

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
#board_world.move((4,5),0)


print(board_world.is_valid_move((2,3)))



print(board_world.board)





