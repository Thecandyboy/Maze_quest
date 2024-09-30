import pygame
from constants import *
import random

pygame.init()

def generate_maze(current_cell,maze):
    current_cell.visited = True
    directions = ['top', 'right', 'bottom', 'left']
    random.shuffle(directions)
    for direction in directions:
        next_cell = None
        if direction == 'top' and current_cell.row > 0:
            next_cell = maze[current_cell.row - 1][current_cell.col]
        elif direction == 'right' and current_cell.col < COLS - 1:
            next_cell = maze[current_cell.row][current_cell.col + 1]
        elif direction == 'bottom' and current_cell.row < ROWS - 1:
            next_cell = maze[current_cell.row + 1][current_cell.col]
        elif direction == 'left' and current_cell.col > 0:
            next_cell = maze[current_cell.row][current_cell.col - 1]
        if next_cell and not next_cell.visited:
            current_cell.walls[direction] = False
            next_cell.walls['top'] = False if direction == 'bottom' else next_cell.walls['top']
            next_cell.walls['right'] = False if direction == 'left' else next_cell.walls['right']
            next_cell.walls['bottom'] = False if direction == 'top' else next_cell.walls['bottom']
            next_cell.walls['left'] = False if direction == 'right' else next_cell.walls['left']
            generate_maze(next_cell, maze)

def render_visible_cells(WINDOW,player, maze):
    visible_cells = []
    player_cell = maze[player.rect.y // CELL_SIZE][player.rect.x // CELL_SIZE]
    for row in range(max(0, player_cell.row - 3), min(ROWS, player_cell.row + 4)):
        for col in range(max(0, player_cell.col - 6), min(COLS, player_cell.col + 7)):
            visible_cells.append(maze[row][col])
    return visible_cells

def draw_visible_cells(WINDOW,visible_cells, camera_x, camera_y):
    for cell in visible_cells:
        cell.draw(WINDOW, camera_x, camera_y)