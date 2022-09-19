import pygame
import game
pygame.init()


def game_over(score):
    W = 1200
    H = 800
    screen = pygame.display.set_mode((W, H))
    font = pygame.font.SysFont('Impact', 30)
    back = pygame.image.load('image/background/background.png').convert_alpha()
    screen.blit(back, (0, 0))
    button_play = pygame.image.load("image/buttons/play_1.png").convert_alpha()
    button_play_rect = button_play.get_rect(center=(W // 2, H // 2 - 300))
    button_exit_rect = button_play.get_rect(center=(W // 2, H // 2 + 300))
    text = font.render(f"Your score: {score}", True, (255, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.game(0)


        if button_play_rect.collidepoint(pygame.mouse.get_pos()):
            button_play = pygame.image.load("image/buttons/play_2.png").convert_alpha()
            if pygame.mouse.get_pressed()[0]:
                game.game(0)
        else:
            button_play = pygame.image.load("image/buttons/play_1.png").convert_alpha()

        if button_exit_rect.collidepoint(pygame.mouse.get_pos()):
            button_exit = pygame.image.load("image/buttons/exit_2.png").convert_alpha()
            if pygame.mouse.get_pressed()[0]:
                exit()
        else:
            button_exit = pygame.image.load("image/buttons/exit_1.png").convert_alpha()


        screen.blit(button_play, button_play_rect)
        screen.blit(button_exit, button_exit_rect)
        screen.blit(text, (500, 200))
        pygame.display.update()