import copy
import sys
import pygame
from constrants import *  # Ensure this module contains necessary constants like WIDTH, HEIGHT, LINE_COLOR, etc.
from cell import Cell  # Assuming Cell class is defined elsewhere to represent individual Sudoku cells.
from sudoku_generator import *

class Board:
    def __init__(self, rows, cols, width, height, difficulty, screen):
        self.width = width
        self.height = height
        self.screen = screen
        self.cols = cols
        self.rows = rows
        self.difficulty = difficulty  # Fixed typo in variable name
        self.board = generate_sudoku(9, self.difficulty)
        self.user_board = copy.deepcopy(self.board)# Fixed initialization call
        self.cells = [[Cell(0, i, j, screen) for j in range(cols)] for i in range(rows)]

        #iterate through our solved board, cell = Cell(board[i][j]
        #for b in board:





        # Removed 'selected_cell' as 'cells' will handle each cell's state

    def print_board(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                print(self.board[i][j], end = ' ')
            print()
    @staticmethod
    def draw(width, height, screen, rows, cols):

        screen.fill(BG_COLOR)
        # Draw the grid lines for the Sudoku board
        size_square = width // 9  # Adjust square size based on the board's width
        for i in range(rows):
            for j in range(cols):
                rect = pygame.Rect(j * size_square, i * size_square, size_square, size_square)
                # Draw thicker line for 3x3 subgrid borders
                if i % 3 == 0 and i != 0:
                    pygame.draw.line(screen, LINE_COLOR, (0, i * size_square), (width, i * size_square), 8)
                if j % 3 == 0 and j != 0:
                    pygame.draw.line(screen, LINE_COLOR, (j * size_square, 0), (j * size_square, height-100), 8)

                # Draw regular grid lines
                pygame.draw.rect(screen, LINE_COLOR, rect, 1)
        pygame.draw.line(screen, LINE_COLOR, (0, 9 * size_square), (width, 9 * size_square), 8)

        """
        # Draw each cell
        for row in self.cells:
            for cell in row:
                cell.Draw()  # Assuming Cell class has a draw method
        """

    # ... other methods like available_square, choose_square, etc. ...

    def selected(self, row, col):
        if self.cells[row][col]. selected:
            return True
    def selected_square(self, row, col):
        self.update_cells()
        self.cells[row][col].selected = True
        self.cells[row][col].draw()
    def mark_square(self, row, col, num):
        self.board[row][col] = num
        self.update_cells()
        self.cells[row][col].draw()
    def update_cells(self):
        self.cells = [[Cell(self.board[i][j], i, j, self.height//self.rows, self.width//self.cols) for j in range(self.cols)] for i in range(self.rows)]

    def final_square(self, row, col):
        self.update_cells()
        self.cells[row][col].draw
    def available_square(self, row, col):
        return self.board[row][col] == 0
    def board_is_full(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 0:
                    return False
        return True
    def reset_board(self):
        self.user_board = copy.deepcopy(self.board)
        #self.update_cells()

    def check_if_winner(self):
        # Check if the board is in a winning state
        for i in range(9):
            if not self.is_unique(self.board[i]):  # Check rows
                return False
            if not self.is_unique([self.board[j][i] for j in range(9)]):  # Check columns
                return False

        # Check 3x3 subgrids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.is_unique([self.board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]):
                    return False

        return True
    def sketch(self, screen):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    number_font = pygame.font.Font(None, 100)
                    number_text = number_font.render(str(self.board[row][col]), 1, (0, 0, 0))
                    number_rect = number_text.get_rect(center=(((WIDTH/9)/2)+ col * WIDTH/9,((HEIGHT-100)/9)/2 + row * (HEIGHT-100)/9))
                    screen.blit(number_text, number_rect)
                else:
                    continue

    def is_unique(self, lst):
        # Helper function to check if all elements in a list are unique (ignoring zeros)
        return len(set(lst)) == len(lst) - lst.count(0)

# ... Rest of the Board class ...

# The event loop and game logic should be in the main part of the program, not inside the Board class.