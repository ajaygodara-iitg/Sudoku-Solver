import streamlit as st
import numpy as np

def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Initialize the board with zeros
board = np.zeros((9, 9), dtype=int)

# Title of the app
st.title("Sudoku Solver")

# Function to draw the Sudoku board
def draw_board(board):
    for row in range(9):
        cols = st.columns(9)
        for col in range(9):
            with cols[col]:
                cell_value = st.text_input(
                    label=f"cell_{row}_{col}",
                    value=str(board[row][col] if board[row][col] != 0 else ""),
                    max_chars=1, 
                    key=f"{row}-{col}",
                    label_visibility="collapsed"
                )
                if cell_value.isdigit() and 1 <= int(cell_value) <= 9:
                    board[row][col] = int(cell_value)
                else:
                    board[row][col] = 0

# Draw the initial board
draw_board(board)

# Solve button
if st.button("Solve Sudoku"):
    if solve_sudoku(board):
        st.success("Sudoku Solved!")
    else:
        st.error("No solution exists!")
    
    # Draw the solved board
    draw_board(board)
