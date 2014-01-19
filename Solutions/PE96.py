# Project Euler 96
# Su Doku
# Kai Kang


########################################
## Solve Sudoku
########################################


solved = [[2,4,8,3,9,5,7,1,6],
          [5,7,1,6,2,8,3,4,9],
          [9,3,6,7,4,1,5,8,2],
          [6,8,2,5,3,9,1,7,4],
          [3,5,9,1,7,4,6,2,8],
          [7,1,4,8,6,2,9,5,3],
          [8,6,3,4,1,7,2,9,5],
          [1,9,5,2,8,6,4,3,7],
          [4,2,7,9,5,3,8,6,1]]

sudoku = [[0,4,8,3,9,0,7,1,0],
          [5,7,0,6,2,0,3,0,9],
          [9,3,6,0,4,1,5,8,2],
          [0,0,2,5,3,0,1,7,4],
          [3,5,9,0,7,4,6,2,8],
          [0,1,4,8,0,2,9,0,3],
          [8,6,3,4,1,7,2,9,5],
          [0,9,0,2,8,0,4,0,7],
          [4,2,0,9,5,3,8,6,1]]

def checkRowAndCol(board, (row, col), number):
    rows, cols = len(board), len(board[0])
    #check in the row
    for i in xrange(cols):
        if board[row][i] == number:
            return False
    # check in the col
    for i in xrange(rows):
        if board[i][col] == number:
            return False
    return True

def checkSquare(board, (row,col), number):
    rows, cols = len(board), len(board[0])
    xLeftBound = (row/3)*3
    xRightBound = xLeftBound + 3
    yLeftBound = (col/3)*3
    yRightBound = yLeftBound + 3
    for row in xrange(rows):
        for col in xrange(cols):
            if xLeftBound <= row < xRightBound:
                if yLeftBound <= col < yRightBound:
                    if board[row][col] == number:
                        return False
    return True

def isLegal(board, (row,col),number):
    return (checkRowAndCol(board,(row,col), number) and
            checkSquare(board, (row,col),number))

def getCons(board):
    rows, cols = len(board), len(board[0])
    ROWS_CONS, COLS_CONS = [], [0]*9
    for row in xrange(rows):
        ROWS_CONS.append(9-board[row].count(0))
        for col in xrange(cols):
            if board[col][row] != 0:
                COLS_CONS[col] += 1
    return ROWS_CONS, COLS_CONS

def guess(board):
    # guess the position with most constraints
    ROWS_CONS, COLS_CONS = getCons(board)
    maxCons,maxConsPos = 0,(0,0)
    rows, cols = len(board), len(board[0])
    for row in xrange(rows):
        for col in xrange(cols):
            if board[row][col] == 0: # valid guess
                constraints = ROWS_CONS[row]+COLS_CONS[col]
                if maxCons < constraints:
                    maxCons = constraints
                    maxConsPos = (row, col)
    return maxConsPos

def countZeros(board):
    rows, cols = len(board), len(board[0])
    count = 0
    for row in xrange(rows):
        for col in xrange(cols):
            if board[row][col] == 0:
                count += 1
    return count

def solveSudoku(board):
    level = countZeros(board)
    return solve(board, level)


def solve(board, level):
    if level == 0:
        return board
    else:
        # try to put 1-9 into the best guess pos
        GUESS = guess(board)
        row, col = GUESS[0], GUESS[1]
        for i in xrange(1,10):
            if isLegal(board, (row,col), i):
                board[row][col] = i
                solution = solve(board,level=level-1)
                if (solution != None):
                    return solution
                board[row][col] = 0
        return None



sudoku_list = []
with open('sudoku.txt', 'r') as f:
    for line in f.readlines():
        if line.startswith("G"):
            try:
                sudoku_list.append(su)
            except:
                pass
            su = []
        else:
            row = []
            for number in line[:-1]:
                row.append(int(number))
            su.append(row)

total = 0
print len(sudoku_list)
"""
for sudoku_puzzle in sudoku_list:
    print "finished"
    solved_puzzle = solveSudoku(sudoku_puzzle)
    number = 100*solved_puzzle[0][0] + 10*solved_puzzle[0][1] + solved_puzzle[0][2]
    total += number
"""
print total
