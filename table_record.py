import pygame
import main
pygame.init()


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

    font = pygame.font.SysFont('Impact', 24)

    block_1 = pygame.image.load("image/buttons/block_1.png").convert_alpha()
    block_1_rect = block_1.get_rect(center=(W//2, 100))
    text_1 = font.render("hello", True, (255, 0, 0))
    block_1.blit(text_1, (75, 50))

    block_2 = pygame.image.load('image/buttons/block_1.png').convert_alpha()
    block_2_rect = block_2.get_rect(center = (W//2, 225))
    text_2 = font.render("hello", True, (255, 0, 0))
    block_2.blit(text_2, (75, 50))

    block_3 = pygame.image.load("image/buttons/block_1.png").convert_alpha()
    block_3_rect = block_1.get_rect(center=(W // 2, 350))
    text_3 = font.render("hello", True, (255, 0, 0))
    block_3.blit(text_3, (75, 50))

    block_4 = pygame.image.load("image/buttons/block_1.png").convert_alpha()
    block_4_rect = block_1.get_rect(center=(W // 2, 475))
    text_4 = font.render("hello", True, (255, 0, 0))
    block_4.blit(text_4, (75, 50))

    block_5 = pygame.image.load("image/buttons/block_1.png").convert_alpha()
    block_5_rect = block_1.get_rect(center=(W // 2, 600))
    text_5 = font.render("hello", True, (255, 0, 0))
    block_5.blit(text_5, (75, 50))

    screen.blit(block_1, block_1_rect)
    screen.blit(block_2, block_2_rect)
    screen.blit(block_3, block_3_rect)
    screen.blit(block_4, block_4_rect)
    screen.blit(block_5, block_5_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if button_back_rect.collidepoint(pygame.mouse.get_pos()):
            button_back = pygame.image.load("image/buttons/back_2.png").convert_alpha()
            if pygame.mouse.get_pressed()[0]:
                main.main_menu()
        else:
            button_back = pygame.image.load("image/buttons/back_1.png").convert_alpha()

        screen.blit(button_back, button_back_rect)
        pygame.display.update()
        clock.tick(FPS)
