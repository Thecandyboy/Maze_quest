import pygame   #we need to import it here also
from constants import * #we need to import here also

class Player():
    def __init__(self,x,y):
        self.rect = pygame.Rect(0,0,PLAYER_WIDTH,PLAYER_HEIGHT)
        self.rect.center = (x,y)
    
    def move (self,dx,dy) :
        self.rect.x += dx 
        self.rect.y += dy 
    
    def draw(self, surface, camera_x, camera_y):
        # Draw the player at its position relative to the camera
        #pygame.draw.rect(surface, RED, (self.rect.x - camera_x, self.rect.y - camera_y, PLAYER_WIDTH, PLAYER_HEIGHT))
        surface.blit(PLAYER_IMG_SCALED,(self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect