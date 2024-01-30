import pygame
from constrants import *

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def get_value(self):
        return self.value
    def set_cell_value(self, value):
        self.value = value
    def set_sketched_value(self, value):
        self.sketched_value = value
    def Draw(self):
        num_font = pygame.font.Font(None, NUM_FONT_SIZE)

        if self.selected:
            pygame.draw.rect(self.screen, BG_COLOR, SQUARE_SIZE * self.col + SQUARE_SIZE//2, SQUARE_SIZE * self.row + SQUARE_SIZE//2 )

        if 1 <= int(self.value) <= 9:
            num = self.value
            number = num_font.render(f'{num}', 1, (255,200,0))
            rend_number = number.get_rect(center = (SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))

            return number, rend_number
