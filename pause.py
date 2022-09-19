import pygame
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

    on_pause = True
    while on_pause:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    on_pause = False

        screen.blit(text, text_rect)
        pygame.display.update()