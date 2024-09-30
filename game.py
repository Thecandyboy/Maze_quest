import pygame
import os
from constants import *
from player import Player
from Level1 import *
from Level2 import *
from Level3 import *
from cell import Cell

pygame.init()
pygame.font.init()
pygame.mixer.init()

MAIN_MENU_FONT = pygame.font.SysFont('comicsans',50) 
CHOOSE_DIFFICULTY_FONT = pygame.font.SysFont('comicsans',40)
LEVEL_FONT = pygame.font.SysFont('comicsans',30)

#Loading the images
OPENING_SCREEN_BG = pygame.image.load(os.path.join('Assets','Opening_Screen_BG.png'))
OPENING_SCREEN_BG_SCALED = pygame.transform.scale(OPENING_SCREEN_BG,(SCREEN_WIDTH,SCREEN_HEIGHT))

#Creating clock to define framerate
clock = pygame.time.Clock() 

#Creating the screen
WINDOW = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("MAZE GAME")

#defining the movement variables
moving_up = False
moving_down = False
moving_left = False
moving_right = False

#Create the player 
player = Player(5,5) 

def main_menu() :
    selected_difficulty = 0 
    running = True 
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if(selected_difficulty == 0 ) :
                        play_level1(player,WINDOW)
                        
                    elif(selected_difficulty == 1 ) :
                        play_level2(player,WINDOW)

                    else :
                        play_level3(player,WINDOW)

                if event.key == pygame.K_DOWN :
                    LEVEL_SWITCH_SOUND.play()
                    selected_difficulty = (selected_difficulty+1)%len(DIFFICULTY)

                if event.key == pygame.K_UP :
                    LEVEL_SWITCH_SOUND.play()
                    selected_difficulty = (selected_difficulty-1)%len(DIFFICULTY)

                if event.key == pygame.K_ESCAPE :
                    running = False
 
                    pygame.quit()
    

        WINDOW.fill(BLACK)
        WINDOW.blit(OPENING_SCREEN_BG_SCALED,(0,0))
        
        main_menu_txt = MAIN_MENU_FONT.render('MAIN MENU',True,RED) 
        difficulty_txt = CHOOSE_DIFFICULTY_FONT.render("CHOOSE DIFFICULTY",True,BLUE)
        
        # Creating Box around DIFFICULTY TEXT
        difficulty_rect = pygame.Rect((SCREEN_WIDTH - difficulty_txt.get_width())//2 -10, (SCREEN_HEIGHT // 4) - 5, difficulty_txt.get_width() + 20 , CHOOSE_DIFFICULTY_FONT.get_height() + 10)
        border_rect1 = difficulty_rect.copy()
        border_rect1.inflate_ip(6, 6) 
        pygame.draw.rect(WINDOW, BLACK, border_rect1, border_radius=5)
        pygame.draw.rect(WINDOW, LIGHT_GRAY, difficulty_rect, border_radius=5)

        # Creating Box around MAIN MENU TEXT
        main_menu_rect = pygame.Rect(SCREEN_WIDTH // 4, (SCREEN_HEIGHT // 12)-5, SCREEN_WIDTH //2, MAIN_MENU_FONT.get_height()+10)
        border_rect2 = main_menu_rect.copy()
        border_rect2.inflate_ip(6, 6) 
        pygame.draw.rect(WINDOW, BLACK, border_rect2, border_radius=5)
        pygame.draw.rect(WINDOW, LIGHT_GRAY, main_menu_rect, border_radius=5)


        # difficulty_rect = pygame.Rect(SCREEN_WIDTH//4 , (SCREEN_HEIGHT // 4)-5, SCREEN_WIDTH//2, CHOOSE_DIFFICULTY_FONT.get_height()+10)        
        level_rects = [
            pygame.Rect(3*SCREEN_WIDTH//8 , 200 + (i + 1) * 140 - 5, SCREEN_WIDTH//4, LEVEL_FONT.get_height()+10)
            for i in range(len(DIFFICULTY))
        ]

        WINDOW.blit(main_menu_txt,((SCREEN_WIDTH-main_menu_txt.get_width())//2,(SCREEN_HEIGHT//12)))
        WINDOW.blit(difficulty_txt,((SCREEN_WIDTH-difficulty_txt.get_width())//2,(SCREEN_HEIGHT//4)))

        for i in range(len(DIFFICULTY)):
            if(i == selected_difficulty) :
                level_txt = LEVEL_FONT.render(DIFFICULTY[i],True,GREEN)
                level_rect = level_rects[i]
                border_rect3 = level_rect.copy()
                border_rect3.inflate_ip(6,6)
                pygame.draw.rect(WINDOW, GREEN , border_rect3, border_radius=5)
                pygame.draw.rect(WINDOW, BLACK, level_rect, border_radius=5)
                WINDOW.blit(level_txt,((SCREEN_WIDTH-level_txt.get_width())//2,(200 + (i+1)*140)))

            else:
                level_txt = LEVEL_FONT.render(DIFFICULTY[i],True,WHITE)
                level_rect = level_rects[i]
                border_rect3 = level_rect.copy()
                border_rect3.inflate_ip(6,6)
                pygame.draw.rect(WINDOW, WHITE , border_rect3, border_radius=5)
                pygame.draw.rect(WINDOW, BLACK, level_rect, border_radius=5)
                WINDOW.blit(level_txt,((SCREEN_WIDTH-level_txt.get_width())//2,(200 + (i+1)*140)))

        pygame.display.flip()

    main_menu()

main_menu()