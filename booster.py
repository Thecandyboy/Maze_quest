import pygame
import random
from constants import *

class Booster:
    def __init__(self, maze):
        self.maze = maze
        self.rect = pygame.Rect(0, 0, CELL_SIZE // 2, CELL_SIZE // 2)
        self.generate_booster()

    def generate_booster(self):
        empty_cells = []
        for row in range(len(self.maze)):
            for col in range(len(self.maze[0])):
                cell = self.maze[row][col]
                if not cell.walls['top'] or not cell.walls['right'] or not cell.walls['bottom'] or not cell.walls['left']:
                    empty_cells.append((row, col))
        
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.rect.topleft = (col * CELL_SIZE + WALL_WIDTH , row * CELL_SIZE + WALL_WIDTH )

    def draw(self, surface, camera_x, camera_y):
        # Draw the coin only if it's within the camera view
        if camera_x <= self.rect.x <= camera_x + WIDTH and camera_y <= self.rect.y <= camera_y + HEIGHT:
            surface.blit(BOOSTER_IMG_SCALED,(self.rect.topleft))