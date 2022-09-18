import pygame
from bullet import Bullet
pygame.init()

class Ship(pygame.sprite.Sprite):
    def __init__(self, file, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.image.blit(pygame.image.load('image/hp_bar/100_hp.png'), (0, 95))
        self.rect = self.image.get_rect(bottomleft=(600, 800))
        self.speed = speed
        self.hp = 500
        self.full_hp = 500
        self.bullets = pygame.sprite.Group()
        self.score = 0

    def left(self):
        self.rect.x -= self.speed

    def right(self):
        self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.x + 50, self.rect.y, self.bullets)
        return bullet

    def hit(self, value):
        self.hp -= value
        if self.hp * 100 / self.full_hp >= 90:
            self.image.blit(pygame.image.load('image/hp_bar/90_hp.png'), (0, 95))
        elif 80 <= self.hp * 100 / self.full_hp < 90:
            self.image.blit(pygame.image.load('image/hp_bar/80_hp.png'), (0, 95))
        elif 70 <= self.hp * 100 / self.full_hp < 80:
            self.image.blit(pygame.image.load('image/hp_bar/70_hp.png'), (0, 95))
        elif 60 <= self.hp * 100 / self.full_hp < 70:
            self.image.blit(pygame.image.load('image/hp_bar/60_hp.png'), (0, 95))
        elif 50 <= self.hp * 100 / self.full_hp < 60:
            self.image.blit(pygame.image.load('image/hp_bar/50_hp.png'), (0, 95))
        elif 40 <= self.hp * 100 / self.full_hp < 50:
            self.image.blit(pygame.image.load('image/hp_bar/40_hp.png'), (0, 95))
        elif 30 <= self.hp * 100 / self.full_hp < 40:
            self.image.blit(pygame.image.load('image/hp_bar/30_hp.png'), (0, 95))
        elif 20 <= self.hp * 100 / self.full_hp < 30:
            self.image.blit(pygame.image.load('image/hp_bar/20_hp.png'), (0, 95))
        elif 10 <= self.hp * 100 / self.full_hp < 20:
            self.image.blit(pygame.image.load('image/hp_bar/10_hp.png'), (0, 95))
        if self.hp <= 0:
            exit()

