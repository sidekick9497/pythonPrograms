#initialize the board
def initializeBoard(size):
    board =[0]*size
    for i in range(size):
        board[i] = [0]*size
    for i in range(size):
        print(board[i])
initializeBoard(4)
"""
def putQueen(startColumn):
    if(startColumn>= BoardSize):
        #we found the solution
        #return board
    if(queenSafeToPlace):
        #place queen
    else:
         # backtracking to previous one    
def queenSafeToPlace(place,board):
   flag = False
   for i in range(size(board)-1):
       if board[place][i]==1:
           return False
       if     
           """