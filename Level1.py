import pygame
import random
import os
from constants import *
from player import Player
from coin import Coin
from booster import Booster
from game_over_screen import *
from cell import *
from maze_renderer import *
from maze_solver import *

pygame.init()
pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()

def play_level1(player,WINDOW):

    #Loading the images
    #MAZE BG
    MAZE_BG = pygame.image.load(os.path.join('Assets',"Maze_BG.jpeg"))
    MAZE_BG_SCALED = pygame.transform.scale(MAZE_BG,(MAZE_WIDTH,MAZE_HEIGHT))
    frame_rem = START_TIME*FPS

    coins_collected = 0
    boosters_collected =0

    player_won = False
    space_ability_used = False

    #intialize maze
    maze = [[Cell(row, col) for col in range(COLS)] for row in range(ROWS)]
    
    # Recursive backtracking algorithm to generate the maze
    start_cell = maze[0][0]
    generate_maze(start_cell,maze)
    
    solution_path = []
    dfs_solve_maze(maze[0][0], maze, solution_path)
    
    #intialising the 4 movements 
    moving_up = False
    moving_down = False
    moving_left = False
    moving_right = False

    current_speed = PLAYER_VEL

    # Initialize coins list and generate coins
    coins = []
    for i in range(NUMBER_OF_COINS):
        new_coin = Coin(maze)
        coins.append(new_coin)

    boosters = []
    for j in range(NUMBER_OF_BOOSTERS_1):
        new_booster = Booster(maze)
        boosters.append(new_booster)

    #FONT STYLES
    TIME_FONT = pygame.font.SysFont('comicsans',30)
    #LEVEL_FONT = pygame.font.SysFont('comicsans',60)
    COINS_COLLECTED_FONT = pygame.font.SysFont('comicsans',30)
    
    running = True 
    while running :
        
        clock.tick(FPS)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
                pygame.quit()

            #General controls
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :   #modify this to main screen
                    return
                # Add coin collection logic
                player_rect = player.get_rect()
                for coin in coins[:]:
                    expanded_coin_rect = coin.rect.inflate(5,5)
                    if player_rect.colliderect(expanded_coin_rect):
                        coins.remove(coin)
                        COIN_COLLECTED_SOUND.play()
                        coins_collected += 1
                for booster in boosters[:] :
                    expanded_booster_rect = booster.rect.inflate(5,5)
                    if player_rect.colliderect(expanded_booster_rect):
                        boosters.remove(booster)
                        BOOSTER_COLLECTED_SOUND.play()
                        boosters_collected += 1 
                        for row in range(ROWS):
                            for col in range(COLS):
                                maze[row][col].draw(WINDOW, 0, 0)
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        
                        frame_rem += TIME_INCREMENT_PER_BOOSTER*FPS
            
            #Player controls
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP :
                    moving_up = True                
                if event.key == pygame.K_DOWN :
                    moving_down = True                
                if event.key == pygame.K_LEFT :
                    moving_left = True  
                if event.key == pygame.K_RIGHT :
                    moving_right = True
                if event.key == pygame.K_SPACE and not space_ability_used:
                    space_ability_start_time = pygame.time.get_ticks()
                    space_ability_used = True

            if event.type == pygame.KEYUP :
                if event.key == pygame.K_UP :
                    moving_up = False
                if event.key == pygame.K_DOWN :
                    moving_down = False              
                if event.key == pygame.K_LEFT :
                    moving_left = False
                if event.key == pygame.K_RIGHT :
                    moving_right = False

        #Player controls
        dx = 0 
        dy = 0
        if moving_up == True :
            dy = -current_speed
        if moving_down == True :
            dy = current_speed
        if moving_left == True :
            dx = -current_speed
        if moving_right == True :
            dx = current_speed
        
        player_rect = player.get_rect()
        for row in maze:
            for cell in row:
                if cell.walls['top'] and player_rect.colliderect(pygame.Rect(cell.col * CELL_SIZE, cell.row * CELL_SIZE, CELL_SIZE,WALL_WIDTH)):
                    player.move(0, current_speed)
                if cell.walls['right'] and player_rect.colliderect(pygame.Rect(cell.col * CELL_SIZE + CELL_SIZE - WALL_WIDTH, cell.row * CELL_SIZE, WALL_WIDTH, CELL_SIZE)):
                    player.move(-current_speed, 0)
                if cell.walls['bottom'] and player_rect.colliderect(pygame.Rect(cell.col * CELL_SIZE, cell.row * CELL_SIZE + CELL_SIZE - WALL_WIDTH, CELL_SIZE, WALL_WIDTH)):
                    player.move(0, -current_speed)
                if cell.walls['left'] and player_rect.colliderect(pygame.Rect(cell.col * CELL_SIZE, cell.row * CELL_SIZE, WALL_WIDTH, CELL_SIZE)):
                    player.move(current_speed, 0)
        
        #move the player
        player.move(dx,dy)
        
        # Calculate camera position to center around the player
        camera_x = max(0, min(player.rect.x - (WIDTH // 2), MAZE_WIDTH - WIDTH))
        camera_y = max(0, min(player.rect.y - (HEIGHT // 2), MAZE_HEIGHT - HEIGHT))
        
        WINDOW.fill(WHITE)
        WINDOW.blit(MAZE_BG_SCALED,(0,0))

        if space_ability_used and pygame.time.get_ticks() - space_ability_start_time < 3000:  #3 sec for level1 
            for row in range(ROWS):
                for col in range(COLS):
                    maze[row][col].draw(WINDOW, 0, 0)  # No camera offset
        else:
            # Draw only the visible portion of the maze based on the player's position
            player_rect = player.get_rect()
            for row in range(max(0, player_rect.y // CELL_SIZE - 4), min(ROWS, player_rect.y // CELL_SIZE + 5)):
                for col in range(max(0, player_rect.x // CELL_SIZE - 4), min(COLS, player_rect.x // CELL_SIZE + 5)):
                    maze[row][col].draw(WINDOW, 0, 0)  # No camera offset
        


        # Draw the coins
        for rem_coin in coins:
            rem_coin.draw(WINDOW,camera_x,camera_y)
        for rem_booster in boosters:
            rem_booster.draw(WINDOW,camera_x,camera_y)

        player.draw(WINDOW, 0, 0)  # No camera offset
        
        
        #check if the player finished 
        if player.rect.collidepoint(FINISH_POINT):
            player_won = True 
            score = (frame_rem//FPS)*100 + coins_collected*200 + boosters_collected*50 + 400 
            if space_ability_used :
                score = max(0,score-200)
            game_over_screen(WINDOW,score,player_won)  # Call the game-over screen function
        
        
        #Checking if time(frames) are still remaining
        frame_rem -= 1 
        if frame_rem < 0 :
            WINDOW.fill(WHITE)
            WINDOW.blit(MAZE_BG_SCALED,(0,0))
            for row in range(ROWS):
                for col in range(COLS):
                    maze[row][col].draw(WINDOW, 0, 0)  # No camera offset
            player.draw(WINDOW, 0, 0)
            for cell in solution_path:
                x = cell.col * CELL_SIZE
                y = cell.row * CELL_SIZE

                pygame.draw.rect(WINDOW, GREEN, (x+10, y+10, CELL_SIZE//2, CELL_SIZE//2))
                pygame.time.wait(60)
                pygame.display.flip()

            pygame.time.wait(5000)
    
            running = False
            score = ((frame_rem+1)*100)//FPS + coins_collected*200 + boosters_collected*50
            if space_ability_used :
                score = max(0,score-200)
            game_over_screen(WINDOW,score,player_won)
            return
        
        #Bottom Live Text
        time_text = TIME_FONT.render("Time Remaining : " + str(frame_rem//60),True,BLUE)
        WINDOW.blit(time_text,(0,720))

        coins_collected_text = COINS_COLLECTED_FONT.render("Coins Collected : " + str(coins_collected),True,BLACK)
        WINDOW.blit(coins_collected_text,((SCREEN_WIDTH-coins_collected_text.get_width()),720))

        pygame.display.flip()
        
    pygame.quit()
