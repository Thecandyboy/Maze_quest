import pygame
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()

VER_PADDING = 80
HOR_PADDING = 0 
SCREEN_WIDTH,SCREEN_HEIGHT = 720,720+VER_PADDING
WIDTH,HEIGHT = 360,360   # This is for the camera
MAZE_WIDTH,MAZE_HEIGHT = 720,720
ROWS, COLS = 20, 20
CELL_SIZE = MAZE_WIDTH // COLS
PLAYER_HEIGHT,PLAYER_WIDTH = 20,20
PLAYER_VEL = 3

WALL_WIDTH = CELL_SIZE // 10

START_TIME = 45 #IN seconds
NUMBER_OF_COINS = 10

NUMBER_OF_BOOSTERS_1 = 6 #for level1
NUMBER_OF_BOOSTERS_2 = 4 #for level2
NUMBER_OF_BOOSTERS_3 = 3 #for level3

TIME_INCREMENT_PER_BOOSTER = 5 #seconds

WHITE =(255,255,255)
BLACK =(0,0,0)
RED =(255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
DARK_GRAY = (140,140,140)
LIGHT_GRAY = (180,180,180)
BG = (40,35,25)
FPS = 60
DIFFICULTY = ["Easy","Medium","Hard"]

FINISH_POINT = (MAZE_WIDTH - PLAYER_WIDTH, MAZE_HEIGHT - PLAYER_HEIGHT)  # Assuming WIDTH and HEIGHT are defined somewhere in your constants file.

#COIN
COIN_IMG = pygame.image.load(os.path.join("Assets","Coin.png"))
COIN_IMG_SCALED = pygame.transform.scale(COIN_IMG,(CELL_SIZE,CELL_SIZE))

#BOOSTER
BOOSTER_IMG = pygame.image.load(os.path.join("Assets","Booster.png"))
BOOSTER_IMG_SCALED = pygame.transform.scale(BOOSTER_IMG,(CELL_SIZE-5,CELL_SIZE-5))

#PLAYER
PLAYER_IMG = pygame.image.load(os.path.join("Assets","Player.png"))
PLAYER_IMG_SCALED = pygame.transform.scale(PLAYER_IMG,(PLAYER_WIDTH,PLAYER_HEIGHT))

#END SCREEN :
END_SCREEN_IMG = pygame.image.load(os.path.join("Assets","Game_over_screen_BG.jpeg"))
END_SCREEN_IMG_SCALED = pygame.transform.scale(END_SCREEN_IMG,(SCREEN_WIDTH,SCREEN_HEIGHT))

#SOUND LOADING
LEVEL_SWITCH_SOUND = pygame.mixer.Sound(os.path.join("Assets","Level_switch.mp3"))
GAME_START_SOUND = pygame.mixer.Sound(os.path.join("Assets","Game_start.mp3"))
COIN_COLLECTED_SOUND = pygame.mixer.Sound(os.path.join("Assets","coin_collected.mp3"))
BOOSTER_COLLECTED_SOUND = pygame.mixer.Sound(os.path.join("Assets","Booster_collected.mp3"))