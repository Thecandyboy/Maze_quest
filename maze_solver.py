import pygame
from constants import *

def dfs_solve_maze(cell, maze, solution_path) :
    if cell.row < 0 or cell.col < 0 or cell.row >= ROWS or cell.col >= COLS or cell.visited2 :
        return False

    cell.visited2 = True
    solution_path.append(cell)  # Append the cell to the solution path
    if cell.row == ROWS - 1 and cell.col == COLS - 1:  # Reached the bottom right corner
        return True

    if not cell.walls['top'] and dfs_solve_maze(maze[cell.row - 1][cell.col], maze, solution_path):
        return True
    if not cell.walls['right'] and dfs_solve_maze(maze[cell.row][cell.col + 1], maze, solution_path):
        return True
    if not cell.walls['bottom'] and dfs_solve_maze(maze[cell.row + 1][cell.col], maze, solution_path):
        return True
    if not cell.walls['left'] and dfs_solve_maze(maze[cell.row][cell.col - 1], maze, solution_path):
        return True
    
    solution_path.pop()
    # Backtrack by removing the last cell from the solution path
    return False