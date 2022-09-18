from game import game
from player import *
import table_record
pygame.init()

def main_menu():
    W = 1200
    H = 800
    level = 0
    screen = pygame.display.set_mode((W, H))
    back = pygame.image.load('image/background/background.png').convert_alpha()
    screen.blit(back, (0, 0))
    button_play = pygame.image.load("image/buttons/play_1.png").convert_alpha()
    button_play_rect = button_play.get_rect(center=(W//2, H//2 - 300))
    button_exit_rect = button_play.get_rect(center=(W//2, H//2 + 300))
    record_table_rect = button_play.get_rect(center=(W//2, H//2))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        btn = pygame.key.get_pressed()
        if btn[pygame.K_KP_ENTER]:
            game(level)
        if button_play_rect.collidepoint(pygame.mouse.get_pos()):
            button_play = pygame.image.load("image/buttons/play_2.png").convert_alpha()
            if pygame.mouse.get_pressed()[0]:
                game(level)

        else:
            button_play = pygame.image.load("image/buttons/play_1.png").convert_alpha()

        if button_exit_rect.collidepoint(pygame.mouse.get_pos()):
            button_exit = pygame.image.load("image/buttons/exit_2.png").convert_alpha()
            if pygame.mouse.get_pressed()[0]:
                exit()
        else:
            button_exit = pygame.image.load("image/buttons/exit_1.png").convert_alpha()

        if record_table_rect.collidepoint(pygame.mouse.get_pos()):
            record_table = pygame.image.load("image/buttons/record_table_2.png").convert_alpha()
            if pygame.mouse.get_pressed()[0]:
                table_record.table_record()
        else:
            record_table = pygame.image.load("image/buttons/record_table_1.png").convert_alpha()


        screen.blit(button_play, button_play_rect)
        screen.blit(button_exit, button_exit_rect)
        screen.blit(record_table, record_table_rect)
        pygame.display.update()

if __name__ == '__main__':
    main_menu()


