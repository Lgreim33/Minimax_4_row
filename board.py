import numpy as np

class Board:
    LENGTH = 6
    HEIGHT = 5
    #terminal case values
    WIN = 1000
    LOSS = -1000
    TIE = 0
    #refernece to board
    board = None
    
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
        
    
    def check_horizontal(self, player):
        """
        Check for 2 or more consecutive 'player' symbols horizontally.
        Return a list of sets of coordinates for any consecutive pieces found.
        """
        consecutive_coords = []
        for r, row in enumerate(self.board):
            start = None
            for c in range(self.board.shape[1]):
                if row[c] == player:
                    if start is None:
                        start = c
                    if c == self.board.shape[1] - 1 and c - start + 1 >= 2:
                        # Add coordinates of the last consecutive pieces
                        consecutive_coords.append([(r, i) for i in range(start, c+1)])
                else:
                    if start is not None and c - start >= 2:
                        consecutive_coords.append([(r, i) for i in range(start, c)])
                    start = None
        return consecutive_coords
    
    def check_vertical(self, player):
        """
        Check for 2 or more consecutive 'player' symbols vertically.
        Return a list of sets of coordinates for any consecutive pieces found.
        """
        consecutive_coords = []
        for c in range(self.board.shape[1]):
            start = None
            for r in range(self.board.shape[0]):
                if self.board[r, c] == player:
                    if start is None:
                        start = r
                    if r == self.board.shape[0] - 1 and r - start + 1 >= 2:
                        # Add coordinates of the last consecutive pieces
                        consecutive_coords.append([(i, c) for i in range(start, r+1)])
                else:
                    if start is not None and r - start >= 2:
                        consecutive_coords.append([(i, c) for i in range(start, r)])
                    start = None
        return consecutive_coords
    
    def check_diagonal_tl_br(self, player):
        consecutive_coords = []
        rows, cols = self.board.shape

        # Only start from the top-left to bottom-right possible diagonal starting points
        for i in range(rows - 1):  # Start rows, but avoid the last rows (not enough space for a diagonal)
            for j in range(cols - 1):  # Start columns, avoiding the last columns
                diag_set = list()
                x, y = i, j
                # Track the diagonal from this starting point
                while x < rows and y < cols and self.board[x][y] == player:
                    diag_set.append((x, y))
                    x += 1
                    y += 1

                # Only add if there are 2 or more consecutive pieces
                if len(diag_set) >= 2:
                    consecutive_coords.append(diag_set)

        return consecutive_coords
                    
                    
                
    
    def check_diagonal_bl_tr(self, player):
        consecutive_coords = []
        rows, cols = self.board.shape

        # Only start from the bottom-left to top-right possible diagonal starting points
        for i in range(1, rows):  # Start from row 1 to the bottom row
            for j in range(cols - 1):  # Start columns, but avoid the last column
                diag_set = list()
                x, y = i, j
                # Track the diagonal from this starting point
                while x >= 0 and y < cols and self.board[x][y] == player:
                    diag_set.append((x, y))
                    x -= 1  # Move upwards
                    y += 1  # Move rightwards

                # Only add if there are 2 or more consecutive pieces
                if len(diag_set) >= 2:
                    consecutive_coords.append(diag_set)

        return consecutive_coords


    
    
    #helper function for heuristic calculation    
    def in_a_row(self,player:bool):
        horizontal = self.check_horizontal(player)
        vertical = self.check_vertical(player)
        bottom_l_top_r = self.check_diagonal_bl_tr(player)
        bottom_r_top_l = self.check_diagonal_tl_br(player)
        
        
        return horizontal,vertical,bottom_l_top_r,bottom_r_top_l
    
    
    def sides_open(self, consecutive_sets):
        
        if len(consecutive_sets) == 0:
            return []
        
        open_space_counts = [0] * len(consecutive_sets)

        for i,p_set in enumerate(consecutive_sets):

            #determine the orientation of the set
            
            #horizontal case
            if(p_set[0][0][0] == p_set[0][1][0]):
                
                left_point = (p_set[0][0][0],p_set[0][0][1]-1)
                right_point =(p_set[0][-1][0],p_set[0][-1][1]+1)
           
                #left open check
                if(self.is_valid_move(left_point)):
                    open_space_counts[i] += 1
                    
                #right open check    
                if(self.is_valid_move(right_point)):
                    open_space_counts[i] += 1
                    
                
                
            #vertical case
            elif(p_set[0][0][1] == p_set[0][1][1]):
                
                top_point = (p_set[0][0][0]-1,p_set[0][0][1])
                bottom_point = (p_set[0][-1][0]+1,p_set[0][-1][1])

                #top check 
                if(self.is_valid_move(top_point)):
                    open_space_counts[i] += 1

                #bottom check
                if(self.is_valid_move(bottom_point)):
                    open_space_counts[i] += 1

            #diagnal case top left to bottom right
            elif p_set[0][0][0] < p_set[0][1][0] and p_set[0][0][1] < p_set[0][1][1]:
                left_point = (p_set[0][0][0]-1,p_set[0][0][1]-1)
                right_point =(p_set[0][-1][0]+1,p_set[0][-1][1]+1)
                
                #left open check
                if(self.is_valid_move(left_point)):
                    open_space_counts[i] += 1
                    
                #right open check    
                if(self.is_valid_move(right_point)):
                    open_space_counts[i] += 1
            
            #diagnal case top right to bottom left    
            elif p_set[0][0][0] > p_set[0][1][0] and p_set[0][0][1] < p_set[0][1][1]:
                left_point = (p_set[0][0][0]+1,p_set[0][0][1]-1)
                right_point =(p_set[0][-1][0]-1,p_set[0][-1][1]+1)
            
                #left open check
                if(self.is_valid_move(left_point)):
                    open_space_counts[i] += 1
                    
                #right open check    
                if(self.is_valid_move(right_point)):
                    open_space_counts[i] += 1

            # Make sure we're working with sets with at least 2 points
            if len(p_set) < 2:
                continue
            
        return open_space_counts
            

 
      
    #calculates the heuristic of the given board state, depending on current player
    def heuristic(self,player:bool):
        
        #check termial cases before calculating the heuristic ie, full board or a player won
   
        two_side_three_row_me = 0
        two_side_three_row_opponent = 0
        one_side_three_row_me = 0
        one_side_three_row_opponent = 0
        two_side_two_row_me = 0
        two_side_two_row_opponent = 0
        one_side_two_row_me = 0
        
        #returns a list of sets, each set is a group of 2-4 points that form a row
        my_consecutive_plays = self.in_a_row(player)
        opponenet_consecutive_plays = self.in_a_row(not player)
        
        print(my_consecutive_plays)
        
        #get the number of sides open for each consecutive set
        my_sides_open = self.sides_open(my_consecutive_plays)
        #opp_sides_open = self.sides_open(opponenet_consecutive_plays)
        print(my_sides_open)
        
        #split these up to read more easily
        heuristic = 200 * two_side_three_row_me - 80 * two_side_three_row_opponent + 150 * one_side_three_row_me
        heuristic = heuristic - 40 * one_side_three_row_opponent + 20 * two_side_two_row_me
        heuristic = heuristic - 15 * two_side_two_row_opponent + 5 * one_side_two_row_me
        
        
        
        return heuristic
        