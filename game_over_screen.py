import pygame
import os
from constants import *
pygame.mixer.init()

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

def game_over_screen(WINDOW,score,player_won):

    #Intialistion of different fonts 
    MAIN_FONT = pygame.font.SysFont('comicsans',60)
    WIN_FONT = pygame.font.SysFont('comicsans',35)
    SCORE_FONT = pygame.font.SysFont('comicsans',50)

    game_over_text = MAIN_FONT.render("GAME OVER",True,WHITE)
    
    win_text = "You WON!!!"
    loss_text = "TIME'S UP ! BETTER LUCK NEXT TIME"
    display_win_text = WIN_FONT.render(win_text,True,GREEN)
    display_loss_text = WIN_FONT.render(loss_text,True,RED)

    running = True 
    while running :
        
        clock.tick(FPS)
        
        WINDOW.fill(BLACK)
        WINDOW.blit(END_SCREEN_IMG_SCALED,(0,0))
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN :  #two options enter for main screen and q to quit the game
                if event.key == pygame.K_SPACE :
                    return
        
        WINDOW.blit(game_over_text,((SCREEN_WIDTH-game_over_text.get_width())//2,100))
        
        if player_won :
            win_rect = pygame.Rect((SCREEN_WIDTH - display_win_text.get_width())//2 - 10, 245 , display_win_text.get_width() + 20 , display_win_text.get_height() + 10)
            border_rect1 = win_rect.copy()
            border_rect1.inflate_ip(6, 6) 
            pygame.draw.rect(WINDOW, BLACK, border_rect1, border_radius=5)
            pygame.draw.rect(WINDOW, LIGHT_GRAY, win_rect, border_radius=5)
            WINDOW.blit(display_win_text,((SCREEN_WIDTH-display_win_text.get_width())//2,250))
        
        else :
            loss_rect = pygame.Rect((SCREEN_WIDTH - display_loss_text.get_width())//2 - 10, 245 , display_loss_text.get_width() + 20 , display_win_text.get_height() + 10)
            border_rect2 = loss_rect.copy()
            border_rect2.inflate_ip(6, 6) 
            pygame.draw.rect(WINDOW, BLACK, border_rect2, border_radius=5)
            pygame.draw.rect(WINDOW, LIGHT_GRAY, loss_rect, border_radius=5)
            WINDOW.blit(display_loss_text,((SCREEN_WIDTH-display_loss_text.get_width())//2,250))

        score_text = SCORE_FONT.render("YOUR SCORE : " + str(score),True,BLUE)
        score_rect = pygame.Rect((SCREEN_WIDTH - score_text.get_width())//2 - 10, 395 , score_text.get_width() + 20 , score_text.get_height() + 10)
        border_rect3 = score_rect.copy()
        border_rect3.inflate_ip(6, 6) 
        pygame.draw.rect(WINDOW, BLACK, border_rect3, border_radius=5)
        pygame.draw.rect(WINDOW, LIGHT_GRAY, score_rect, border_radius=5)
        WINDOW.blit(score_text,((SCREEN_WIDTH-score_text.get_width())//2,400))

        pygame.display.flip()
    
    pygame.quit()