import pygame

import bullet
from player import Ship
import Enemy
from bullet import Bullet
pygame.init()

def upgrade(obj):
    W = 1200
    H = 800
    screen = pygame.display.set_mode((W, H))
    back = pygame.image.load('image/background/background.png').convert_alpha()
    screen.blit(back, (0, 0))
    font = pygame.font.SysFont('Impact', 100)
    font_price = pygame.font.SysFont('Impact', 50)
    heal = pygame.image.load('image/buttons/heal_1.png')
    heal_rect = heal.get_rect(center=(400, 200))
    up = pygame.image.load('image/buttons/up_1.png')
    up_rect = up.get_rect(center = (400, 325))
    gun = pygame.image.load('image/buttons/gun_1.png')
    gun_rect = gun.get_rect(center=(400, 450))
    l_up = pygame.image.load('image/buttons/lup_1.png')
    l_up_rect = l_up.get_rect(center=(400, 575))


    on_pause = True
    while on_pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    on_pause = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and heal_rect.collidepoint(pygame.mouse.get_pos()):
                    Ship.heal(obj)
                if event.button == 1 and up_rect.collidepoint(pygame.mouse.get_pos()):
                    Ship.upgrade(obj)
                if event.button == 1 and l_up_rect.collidepoint(pygame.mouse.get_pos()):
                    Enemy.Enemy.level_up(obj)
                if event.button == 1 and gun_rect.collidepoint(pygame.mouse.get_pos()):
                    Bullet.upgrade(obj)


        if heal_rect.collidepoint(pygame.mouse.get_pos()):
            heal = pygame.image.load("image/buttons/heal_2.png").convert_alpha()
        else:
            heal = pygame.image.load("image/buttons/heal_1.png").convert_alpha()

        if up_rect.collidepoint(pygame.mouse.get_pos()):
            up = pygame.image.load("image/buttons/up_2.png").convert_alpha()
        else:
            up = pygame.image.load("image/buttons/up_1.png").convert_alpha()

        if gun_rect.collidepoint(pygame.mouse.get_pos()):
            gun = pygame.image.load("image/buttons/gun_2.png").convert_alpha()
        else:
            gun = pygame.image.load("image/buttons/gun_1.png").convert_alpha()

        if l_up_rect.collidepoint(pygame.mouse.get_pos()):
            l_up = pygame.image.load("image/buttons/lup_2.png").convert_alpha()
        else:
            l_up = pygame.image.load("image/buttons/lup_1.png").convert_alpha()


        heal_price = font_price.render(f"{(obj.full_hp - obj.hp) * 5}", True, (255, 0, 0))
        up_price = font_price.render(f"{Ship.price[Ship.level]+(obj.full_hp - obj.hp) * 5}", True, (255, 0, 0))
        level_up = font_price.render(f"{Enemy.Enemy.price[Enemy.Enemy.level]}", True, (255, 0, 0))
        gun_up = font_price.render(f"{Bullet.price[Bullet.level]}", True, (255, 0, 0))

        score = font.render(f"Score: {obj.score}", True, (255, 0, 0))

        screen.blit(up, up_rect)
        screen.blit(heal, heal_rect)
        screen.blit(gun, gun_rect)
        screen.blit(l_up, l_up_rect)

        screen.blit(heal_price, (500, 175))
        screen.blit(up_price, (500, 300))
        screen.blit(gun_up, (500, 425))
        screen.blit(level_up, (500, 550))
        screen.blit(score, (450, 0))

        pygame.display.update()
        screen.blit(back, (0, 0))
