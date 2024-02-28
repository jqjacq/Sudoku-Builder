import numpy as np
import random
### 0. CREATE SUDOKU BOARD (9x9) ###
def create_sudoku_board():
    board = np.zeros((9, 9), dtype=int) #.zeros: creates an array of zeros
    return board
### 1. SEPERATE BOARD INTO 3x3 SQUARES ###
def display_sudoku_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 22)  # Print horizontal line after every 3 rows
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Print vertical line after every 3 columns
            print(board[i][j], end=" ")
        print()
### 2. CHECK VALIDITY (ENSURE NO REPEATING NUMBERS IN ROW, COLUMN, OR 3x3 SQUARE) ###
def check_validity(board, row, col, num):
    return ( #.any: returns True if any of the elements is True
        not np.any(board[row, :] == num) and #Makes sure number is not in the same row
        not np.any(board[:, col] == num) and #Makes sure number is not in the same column
        not np.any(board[(row//3)*3:(row//3)*3+3, (col//3)*3:(col//3)*3+3] == num) #Make sure number is not in same 3x3 square
    )
### 3. CREATE SOLVED SUDOKU BOARD ###
def solved_sudoku_board(board):
    def find_empty_cell(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None    
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True # Puzzle solved successfully
    
    row, col = empty_cell #Find the first empty cell

    for num in range(1, 10): #Placing numbers 1-9 in the empty cell
        if check_validity(board, row, col, num):
            board[row, col] = num

            if solved_sudoku_board(board): #Recursively try to solve the remaining puzzle
                return True
            board[row, col] = 0 #Backtrack if unable to solve with current number
    return False #Unable to solve puzzle
### 4. RANDOMIZE THE BOARD ###
def choose_sudoku_level(difficulty): # Generate the Sudoku Puzzle based on difficulty level
    board = create_sudoku_board() #Create the Sudoku Board
    solved_sudoku_board(board) #Solve the Sudoku Puzzle

    # Randomly remove numbers to create the puzzle based on difficulty
    if difficulty == "easy" or difficulty == "1": 
        remove_count = 40
    elif difficulty == "medium" or difficulty == "2":
        remove_count = 50
    elif difficulty == "hard" or difficulty == "3":
        remove_count = 60
    else:
        raise ValueError("Invalid difficulty level")

    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells) #Randomize the board

    for i in range(remove_count):
        row, col = cells[i]
        board[row][col] = 0  # Remove numbers from the board
    return board

if __name__ == "__main__":
    difficulty = input("Choose difficulty (easy, medium, hard): ")
    sudoku_board = choose_sudoku_level(difficulty)
    sudoku_board = np.where(sudoku_board == 0, " ", sudoku_board) #Remove the 0s from the board
    print(f"SUDOKU", f"Level:{difficulty.capitalize()}".rjust(15))
    display_sudoku_board(sudoku_board)
