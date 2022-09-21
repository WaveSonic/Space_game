import pygame
from main import main_menu
pygame.init()

def pause():
    W = 1200
    H = 800
    screen = pygame.display.set_mode((W, H))
    back = pygame.image.load('image/background/background.png').convert_alpha()
    screen.blit(back, (0, 0))
    font = pygame.font.SysFont('Impact', 100)
    text = font.render("PAUSE", True, (255, 0, 0))
    text_rect = text.get_rect(center=(W//2, H//2))
    button_play = pygame.image.load("image/buttons/play_1.png").convert_alpha()
    button_exit_rect = button_play.get_rect(center=(W // 2, H // 2 + 300))
    button_play_rect = button_play.get_rect(center=(W // 2, H // 2 - 300))

    on_pause = True
    while on_pause:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    on_pause = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and button_exit_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.display.update()
                    main_menu()

        if button_exit_rect.collidepoint(pygame.mouse.get_pos()):
            button_exit = pygame.image.load("image/buttons/exit_2.png").convert_alpha()
        else:
            button_exit = pygame.image.load("image/buttons/exit_1.png").convert_alpha()

        screen.blit(button_exit, button_exit_rect)
        screen.blit(text, text_rect)
        pygame.display.update()