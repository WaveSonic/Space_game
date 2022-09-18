import pygame
pygame.init()
from game import game

def table_record():
    W = 1200
    H = 800
    screen = pygame.display.set_mode((W, H))
    FPS = 60
    clock = pygame.time.Clock()
    back = pygame.image.load('image/background/background.png').convert_alpha()
    screen.blit(back, (0, 0))
    button_back = pygame.image.load("image/buttons/back_1.png").convert_alpha()
    button_back_rect = button_back.get_rect(topleft=(10, 10))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if button_back_rect.collidepoint(pygame.mouse.get_pos()):
            button_back = pygame.image.load("image/buttons/back_2.png").convert_alpha()
            if pygame.mouse.get_pressed()[0]:
                game(0)
        else:
            button_back = pygame.image.load("image/buttons/back_1.png").convert_alpha()

        screen.blit(button_back, button_back_rect)
        pygame.display.update()
        clock.tick(FPS)
