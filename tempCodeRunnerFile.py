difficulty_rect = pygame.Rect((SCREEN_WIDTH - difficulty_txt.get_width())//2 -10, (SCREEN_HEIGHT // 4) - 5, difficulty_txt.get_width() + 20 , CHOOSE_DIFFICULTY_FONT.get_height() + 10)
        border_rect1 = difficulty_rect.copy()
        border_rect1.inflate_ip(6, 6) 
        pygame.draw.rect(WINDOW, BLACK, border_rect1, border_radius=5)
        pygame.draw.rect(WINDOW, LIGHT_GRAY, difficulty_rect, border_radius=5)
