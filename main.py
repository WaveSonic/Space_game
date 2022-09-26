import pygame.mixer
import game
import sys
from player import *
import table_record
pygame.init()
kn = pygame.mixer.Sound('sound/zvuk11.wav')
kn.set_volume(0.6)

level = 0
def main_menu():
    kn1 = kn2 = kn3 = False
    W = 1200
    H = 800
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
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and button_exit_rect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()

        btn = pygame.key.get_pressed()
        if btn[pygame.K_KP_ENTER]:
            game.game()
        if button_play_rect.collidepoint(pygame.mouse.get_pos()):
            if kn1 == False:
                kn.play()
            kn1 = True
            button_play = pygame.image.load("image/buttons/play_2.png").convert_alpha()
            if pygame.mouse.get_pressed()[0]:
                game.game()

        else:
            button_play = pygame.image.load("image/buttons/play_1.png").convert_alpha()
            kn1 = False

        if button_exit_rect.collidepoint(pygame.mouse.get_pos()):
            if kn2 == False:
                kn.play()
            kn2 = True
            button_exit = pygame.image.load("image/buttons/exit_2.png").convert_alpha()
        else:
            button_exit = pygame.image.load("image/buttons/exit_1.png").convert_alpha()
            kn2 = False

        if record_table_rect.collidepoint(pygame.mouse.get_pos()):
            record_table = pygame.image.load("image/buttons/record_table_2.png").convert_alpha()
            if kn3 == False:
                kn.play()
            kn3 = True
            if pygame.mouse.get_pressed()[0]:
                table_record.table_record()
        else:
            record_table = pygame.image.load("image/buttons/record_table_1.png").convert_alpha()
            kn3 = False



        screen.blit(button_play, button_play_rect)
        screen.blit(button_exit, button_exit_rect)
        screen.blit(record_table, record_table_rect)
        pygame.display.update()

if __name__ == '__main__':
    main_menu()


