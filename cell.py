import pygame
from constants import *

pygame.init()

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False
        self.visited2 = False
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}

    def draw(self, screen, camera_x, camera_y):
        x = self.col * CELL_SIZE - camera_x
        y = self.row * CELL_SIZE - camera_y
        if self.walls['top']:
            pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, WALL_WIDTH))
        if self.walls['right']:
            pygame.draw.rect(screen, WHITE, (x + CELL_SIZE - WALL_WIDTH, y, WALL_WIDTH, CELL_SIZE))
        if self.walls['bottom']:
            pygame.draw.rect(screen, WHITE, (x, y + CELL_SIZE - WALL_WIDTH, CELL_SIZE, WALL_WIDTH))
        if self.walls['left']:
            pygame.draw.rect(screen, WHITE, (x, y, WALL_WIDTH, CELL_SIZE))